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


Models
------

The COVID-Net CT-1 L model is downloaded from
https://github.com/haydengunraj/COVIDNet-CT/blob/master/docs/models.md


Local Build
-----------

.. code:: bash

    DOCKER_BUILDKIT=1 docker build -t local/pl-ct-covidnet .

Run
----

.. code:: bash

    docker run --rm -v $PWD/in:/incoming -v $PWD/out:/outgoing    \
        darwinai/covidnet-pl-ct ct-covidnet                          \
            --imagefile ex-covid-ct.jpg /incoming /outgoing
