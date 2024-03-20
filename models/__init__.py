#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE', 'file').lower()
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
try:
    storage.reload()
except Exception as e:
    print(f"Failed to reload data from storage: {e}")
