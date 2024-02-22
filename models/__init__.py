#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'dp':
    from engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
