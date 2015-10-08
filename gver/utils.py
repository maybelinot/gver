#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-11 10:57:06
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-10-08 15:42:00

from __future__ import unicode_literals, absolute_import

import logging
import os
import subprocess
import sys

import yaml
from oauth2client import file, client, tools

# Load logging before anything else
logging.basicConfig(format='>> %(message)s')
logr = logging.getLogger('members')

# History file
CONFIG_FILE = os.path.expanduser('~/.gver')
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as _:
        config = yaml.load(_)
    if config is None:
        config = {}
else:
    config = {}


''' Load the file with credentials '''
CLIENT_SECRET_FILE = os.path.expanduser('~/.gdrive_private')

DEFAULT_TOKEN = os.path.expanduser('~/.oauth/drive.json')

SCOPES = ('https://www.googleapis.com/auth/drive.metadata.readonly '
          'https://www.googleapis.com/auth/drive '
          'https://spreadsheets.google.com/feeds '
          'https://docs.google.com/feeds')


def update_config(dct):
    with open(CONFIG_FILE, "w") as _:
        yaml.dump(dct, _)


def run(cmd):
    cmd = cmd if isinstance(cmd, list) else cmd.split()
    try:
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as error:
        logr.error("'{0}' failed: {1}".format(cmd, error))
        raise
    output, errors = process.communicate()
    if process.returncode != 0 or errors:
        if output:
            logr.error(output)
        if errors:
            logr.error(errors)
        sys.exit(process.returncode)
    return output, errors


def get_credentials():
    '''Docs'''
    from gutile import utils

    return utils.get_credentials(CLIENT_SECRET_FILE,
                                 DEFAULT_TOKEN,
                                 SCOPES)
