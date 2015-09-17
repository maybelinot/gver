#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-16 11:28:21
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-09-17 14:09:00


import os
import sys
from string import ascii_uppercase
import httplib2

from apiclient import discovery

from utils import logr

try:
    input = raw_input
except NameError:  # Python 3
    pass


def history(credentials=None, file_id=None):
    '''
    FIXME DOCs
    '''
    http = credentials.authorize(httplib2.Http())
    # FIXME: Different versions have different keys like v1:id, v2:fileId
    service = discovery.build('drive', 'v2', http=http)

    try:
        revisions = service.revisions().list(fileId=file_id).execute()
        return revisions.get('items', [])
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
    return None

