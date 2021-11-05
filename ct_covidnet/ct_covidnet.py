#!/usr/bin/env python
#
# ct_covidnet ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp

from ct_covidnet.run_covidnet_ct import RunAnalysis

Gstr_title = """

Generate a title from 
http://patorjk.com/software/taag/#p=display&f=Doom&t=ct_covidnet

"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       ct_covidnet.py 

    SYNOPSIS

        python ct_covidnet.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir in out && chmod 777 out
            python ct_covidnet.py   \\
                                in    out

    DESCRIPTION

        `ct_covidnet.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 

"""


class Ct_covidnet(ChrisApp):
    """
    Plugin to ChRIS for CT-COVID-Net functionalities.
    """
    PACKAGE = __package__
    TITLE = 'COVID-Net inference for chest x-ray'
    CATEGORY = ''
    TYPE = 'ds'
    ICON = ''  # url of an icon image
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = '1Gi'  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--imagefile',
                          dest='imagefile',
                          type=str,
                          optional=False,
                          help='Name of CT image file to infer from')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        options.model_dir = os.path.join(
            '/usr/local/lib/ct-covidnet/COVID-Net_CT-1_L')
        options.meta_name = 'model.meta'
        options.ckpt_name = 'model'
        options.input_width = 512
        options.input_height = 512
        RunAnalysis.run_analysis(options)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# chris app needs to write to files as outputs and taking inputs
# output a dicom image then ChRIS user interface will be able to show it
# csv, json, or custom html css files
