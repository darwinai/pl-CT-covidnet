pl-CT-covidnet
================================

.. image:: https://badge.fury.io/py/ct_covidnet.svg
    :target: https://badge.fury.io/py/ct_covidnet

.. image:: https://travis-ci.org/FNNDSC/ct_covidnet.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/ct_covidnet

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-ct_covidnet

.. contents:: Table of Contents


Abstract
--------

This ia an app to run COVID-Net CT models on chest CT images.

Synopsis
--------

.. code::

    python ct_covidnet.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        [--imagefile]                                               \
        <inputDir>
        <outputDir> 

Description
-----------

``ct_covidnet.py`` is a ChRIS-based plugin for the COVIDNet-UI that performs classification of COVID-19 from chest CT images. More details on the implementation can be found on the paper, `COVIDNet-CT: A Tailored Deep Convolutional Neural Network Design for Detection of COVID-19 Cases from Chest CT Images <https://arxiv.org/abs/2009.05383>`_.

Arguments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.

    [--imagefile]
    required, name of the image file to be analyzed 


Setup
----

Download the pre-trained Machine learning model from: 
https://drive.google.com/drive/folders/13Cb8yvAW0V_Hh-AvUEDrMEpwLhD3zv-F

Make sure to download the COVIDNet-CT-A folder and put it in ct_covidnet/models.

The folder structure should be:

pl-covidnet/ct_covidnet/models/COVIDNet-CT-A


Run
----

This ``plugin`` can be run as a containerized Docker image.


Build Docker image
~~~~~~~~~~~~~~~~~~~~

docker build -t local/pl-ct-covidnet .



Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*.

Prefix all calls with: 

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            local/pl-ct-covidnet ct_covidnet.py                        \
            --imagefile ex-covid-ct.png
            /incoming /outgoing

Examples
--------


python3 ct_covidnet/ct_covidnet.py --imagefile ex-covid-ct.png in out

docker run --rm -v /json:/json local/pl-ct-covidnet ct_covidnet.py --savejson /json
