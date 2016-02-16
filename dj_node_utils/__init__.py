# -*- coding: utf-8 -*-
__version__ = '0.1.0'

import os
from django.contrib.staticfiles.finders import get_finders

def get_static_paths():
    static_paths = []
    for finder in get_finders():
        try:
            storages = finder.storages
        except AttributeError:
            continue
        for storage in storages.values():
            try:
                path = storage.path('.')
                if os.path.isdir(path):
                    static_paths.append(storage.path('.'))
            except NotImplementedError:
                # storages that do not implement 'path' do not store files locally,
                # and thus cannot provide an include path
                pass
    return static_paths
