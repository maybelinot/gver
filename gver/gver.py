#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-16 11:28:21
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-10-08 11:48:37


import os
import sys
from string import ascii_uppercase
import httplib2

from apiclient import errors
from apiclient import discovery
from apiclient.http import MediaIoBaseUpload
from StringIO import StringIO

from utils import logr


def update_file(service, file_id, data):
    """Update an existing file's metadata and content."""
    try:
        media_data, meta_data = data
        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body=meta_data,
            newRevision=True,
            media_body=media_data).execute()
        return updated_file
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return None


def get_file(http, file_id):
    """Print a file's content"""
    try:
        service = discovery.build('drive', 'v2', http=http)
        meta_data = service.files().get(fileId=file_id).execute()

        url = meta_data['exportLinks']['text/html']
        response, content = http.request(url)
        media_data = MediaIoBaseUpload(
            StringIO(content), 'text/html', resumable=False)
        return media_data, meta_data
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
