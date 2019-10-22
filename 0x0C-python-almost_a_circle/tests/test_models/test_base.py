#!/usr/bin/python3
"""Provides unittest for the 'Base' class provided by the 'models' module
"""

import unittest
import json

from models.base import Base


class TestBase(unittest.TestCase):
    """Test base model methods
    """
    def setUp(self):
        self.base = Base()

    def test_base(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.base, Base)

    def test_base_id(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.base.id, int)
        self.assertGreater(self.base.id, 0)

    def test_init_type(self):
        """Test the __init__ method
        """
        types = (int, float, str, tuple, list, dict, set, bool)
        self.assertIsInstance(Base(), Base)
        self.assertIsInstance(Base(0), Base)
        for value in [t() for t in types] + [None, type]:
            self.assertIsInstance(Base(id=value), Base)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        types = (int, float, str, tuple, list, dict, set, bool)
        self.assertNotEqual(self.base.id, Base().id)
        self.assertNotEqual(self.base.id, Base(id=None).id)
        self.assertEqual(Base(0).id, 0)
        for value in (t() for t in types):
            self.assertEqual(Base(id=value).id, value)

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Base(id=type).id, type)

    def test_init_id_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Base().id, int)
        self.assertIsInstance(Base(id=None).id, int)

    def test_init_raises(self):
        """Test the __init__ method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) takes from 1 to 2 positional arguments\\b.*",
            Base, 0, 0
        )

    def test_create_type(self):
        """Test the create method
        """
        types = (int, float, str, tuple, list, dict, set, bool)
        self.assertIsInstance(Base.create(), Base)
        for value in [t() for t in types] + [None, type]:
            self.assertIsInstance(Base.create(id=value), Base)

    def test_create_id_equality(self):
        """Test the create method
        """
        types = (int, float, str, tuple, list, dict, set, bool)
        self.assertNotEqual(self.base.id, Base.create().id)
        for value in (t() for t in types):
            self.assertEqual(Base.create(id=value).id, value)

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Base.create(id=None).id, None)
        self.assertIs(Base.create(id=type).id, type)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Base.create().id, int)

    def test_create_raises(self):
        """Test the create method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Base.create, 0
        )

    def test_to_json_string_equality_defaults(self):
        """Test the to_json_string method
        """
        types = (int, float, str, tuple, list, dict, bool)
        self.assertEqual(Base.to_json_string(None), json.dumps([]))
        for value in (t() for t in types):
            self.assertEqual(Base.to_json_string(value), json.dumps(value))
            self.assertEqual(Base.to_json_string([value]), json.dumps([value]))

    def test_to_json_string_equality(self):
        """Test the to_json_string method
        """
        values = ([{}], [{}, {}], [{'a': 1}], [{'a': 1}, {'a': 2, 'b': 3}])
        for value in values:
            self.assertEqual(Base.to_json_string(value), json.dumps(value))
