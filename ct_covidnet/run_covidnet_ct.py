
"""
Training/testing/inference script for COVIDNet-CT model for COVID-19 detection in CT images.
"""

import os
import sys
import cv2
import json
import numpy as np
from math import ceil
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from data_utils import auto_body_crop

# Dict keys
TRAIN_OP_KEY = 'train_op'
TF_SUMMARY_KEY = 'tf_summaries'
LOSS_KEY = 'loss'

# Tensor names
IMAGE_INPUT_TENSOR = 'Placeholder:0'
LABEL_INPUT_TENSOR = 'Placeholder_1:0'
CLASS_PRED_TENSOR = 'ArgMax:0'
CLASS_PROB_TENSOR = 'softmax_tensor:0'
TRAINING_PH_TENSOR = 'is_training:0'
LOSS_TENSOR = 'add:0'

# Names for train checkpoints
CKPT_NAME = 'model.ckpt'
MODEL_NAME = 'COVIDNet-CT'

# Output directory for storing runs
OUTPUT_DIR = 'output'

# Class names ordered by class index
CLASS_NAMES = ('Normal', 'Pneumonia', 'COVID-19')

def create_session():
    """Helper function for session creation"""
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    return sess


class COVIDNetCTRunner:
    """Primary training/testing/inference class"""
    def __init__(self, meta_file, ckpt=None, data_dir=None, input_height=224, input_width=224, max_bbox_jitter=0.025,
                 max_rotation=10, max_shear=0.15, max_pixel_shift=10, max_pixel_scale_change=0.2):
        self.meta_file = meta_file
        self.ckpt = ckpt
        self.input_height = input_height
        self.input_width = input_width
        self.dataset = None

    def infer(self, image_file):
        image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

        image = cv2.resize(image, (self.input_width, self.input_height), cv2.INTER_CUBIC)
        image = image.astype(np.float32) / 255.0
        image = np.expand_dims(np.stack((image, image, image), axis=-1), axis=0)

        # Create feed dict
        feed_dict = {IMAGE_INPUT_TENSOR: image, TRAINING_PH_TENSOR: False}
        
        # Run inference
        graph, sess, saver = self.load_graph()
        with graph.as_default():
            # Load checkpoint
            self.load_ckpt(sess, saver)

            # Run image through model
            class_, probs = sess.run([CLASS_PRED_TENSOR, CLASS_PROB_TENSOR], feed_dict=feed_dict)
            print('\nPredicted Class: ' + CLASS_NAMES[class_[0]])
            print('Confidences:' + ', '.join(
                '{}: {}'.format(name, conf) for name, conf in zip(CLASS_NAMES, probs[0])))

    def load_ckpt(self, sess, saver):
        """Helper for loading weights"""
        # Load weights
        if self.ckpt is not None:
            print('Loading weights from ' + self.ckpt)
            saver.restore(sess, self.ckpt)

    def load_graph(self):
        """Creates new graph and session"""
        graph = tf.Graph()
        with graph.as_default():
            # Create session and load model
            sess = create_session()

            # Load meta file
            print('Loading meta graph from ' + self.meta_file)
            saver = tf.train.import_meta_graph(self.meta_file)
        return graph, sess, saver

class RunAnalysis:

  @staticmethod
  def run_analysis(args):
    # Suppress most console output
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    meta_file = os.path.join(args.model_dir, args.meta_name)
    ckpt = os.path.join(args.model_dir, args.ckpt_name)

    augmentation_kwargs = {}
    runner = COVIDNetCTRunner(
        meta_file,
        ckpt=ckpt,
        input_height=args.input_height,
        input_width=args.input_width,
        **augmentation_kwargs # unpacks a dictionary into keyword arguments.
    )

    runner.infer(args.imagefile)