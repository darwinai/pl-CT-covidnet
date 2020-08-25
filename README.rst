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

An app to run COVID-Net CT modles on image files


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

``ct_covidnet.py`` is a ChRIS-based application that...

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

Make sure to download the COVIDNet-CT-A folder

Then put the downloaded folders in ct_covidnet/models

The folder structure should be:

pl-covidnet/ct_covidnet/models/COVIDNet-CT-A


Run
----

This ``plugin`` can be run as a containerized docker image.


Build Docker image
~~~~~~~~~~~~~~~~~~~~

docker build -t local/pl-ct-covidnet .



Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            local/pl-ct-covidnet ct_covidnet.py                        \
            --imagefile ex-covid-ct.png
            /incoming /outgoing

Examples
--------


python3 ct_covidnet/ct_covidnet.py --imagefile ex-covid-ct.png in out

docker run --rm -v /json:/json local/pl-ct-covidnet ct_covidnet.py --savejson /json
