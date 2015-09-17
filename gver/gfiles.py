#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-16 11:54:47
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-09-17 14:06:56

import re
import httplib2

from apiclient import discovery


def get_file_id(credentials, gfile, write_access=False):
    """DOCS..."""
    # auth for apiclient
    http = credentials.authorize(httplib2.Http())
    # FIXME: Different versions have different keys like v1:id, v2:fileId
    service = discovery.build('drive', 'v2', http=http)
    about = service.about().get().execute()

    file_id = about['rootFolderId']
    pathway = gfile.split('/')

    if write_access:
        f_types = ['folder'] * (len(pathway) - 1) + ['spreadsheet']
        f_types = ['application/vnd.google-apps.' + f for f in f_types]

    # folder/folder/folder/spreadsheet
    for idx, name in enumerate(pathway):
        if name == '':
            continue
        file_exists = False
        # searching for all files in gdrive with given name
        files = service.files().list(
            q="title = '%s'" % (name,)).execute()['items']
        for f in files:
            # if file not trashed and previos file(or root for first
            # file) in parents then remember file id
            if not f['labels']['trashed'] and \
                    any([file_id in parent['id'] for parent in f['parents']]):
                file_id = f['id']
                file_exists = True
                break
        #  else error
        if not file_exists:
            if write_access == True:
                body = {
                    'mimeType': f_types[idx],
                    'title': name,
                    'parents': [{"id": file_id}]
                }
                file_id = service.files().insert(
                    body=body).execute(http=http)['id']
            else:
                return None
    return file_id


def delete_file(credentials, file_id):
    """DOCS..."""
    try:
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v2', http=http)
        service.files().delete(fileId=file_id).execute()
    except errors.HttpError, error:
        raise RuntimeError('An error occurred: %s' % error)
