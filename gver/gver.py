#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-16 11:28:21
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-10-06 15:53:46


import os
import sys
from string import ascii_uppercase
import httplib2

from apiclient import errors
from apiclient import discovery
from apiclient.http import MediaIoBaseUpload
from StringIO import StringIO

from utils import logr


def update_file(service, file_id, media_body):
    """Update an existing file's metadata and content.

    Args:
      service: Drive API service instance.
      file_id: ID of the file to update.
      new_title: New title for the file.
      new_description: New description for the file.
      new_mime_type: New MIME type for the file.
      new_filename: Filename of the new content to upload.
      new_revision: Whether or not to create a new revision for this file.
    Returns:
      Updated file metadata if successful, None otherwise.
    """
    try:
        # First retrieve the file from the API.
        file = service.files().get(fileId=file_id).execute()
        print(file)
        # File's new content.
        # media_body = MediaFileUpload(
        #     new_filename, mimetype=new_mime_type, resumable=True)

        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body=file,
            newRevision=True,
            media_body=media_body).execute()
        return updated_file
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return None


def get_file_content(http, file_id):
    """Print a file's content.

    Args:
      service: Drive API service instance.
      file_id: ID of the file.

    Returns:
      File's content if successful, None otherwise.
    """
    try:
        service = discovery.build('drive', 'v2', http=http)

        url = service.files().get(fileId=file_id).execute()[
            'exportLinks']['text/html']
        response, content = http.request(url)
        print(content)
        media_body = MediaIoBaseUpload(
            StringIO(content), 'text/html', resumable=False)
        return media_body
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
