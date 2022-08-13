#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb
import models

@unittest.skipIf(
       os.getenv('HBNB_TYPE_STORAGE') != 'db',
       "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage"""

    @classmethod
    def setUpClass(cls):
        """Tests"""
        cls.user = User()
        cls.user.first_name = "Lufy"
        cls.user.last_name = "Monkey"
        cls.user.email = "OnePiece@hotmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """tests if all works in DB Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_reload_dbtorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""


if __name__ == "__main__":
    unittest.main()