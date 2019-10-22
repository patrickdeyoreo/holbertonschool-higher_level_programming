#!/usr/bin/python3
"""Provides unittest for the 'Base' class provided by the 'models' module
"""

import unittest

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
        self.assertIsInstance(Base(), Base)
        self.assertIsInstance(Base(id=None), Base)
        self.assertIsInstance(Base(0), Base)
        self.assertIsInstance(Base(id=0), Base)
        self.assertIsInstance(Base(id=0.0), Base)
        self.assertIsInstance(Base(id="0"), Base)
        self.assertIsInstance(Base(id=(0,)), Base)
        self.assertIsInstance(Base(id=[0]), Base)
        self.assertIsInstance(Base(id={0}), Base)
        self.assertIsInstance(Base(id={0: 0}), Base)
        self.assertIsInstance(Base(id=True), Base)
        self.assertIsInstance(Base(id=type), Base)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        self.assertNotEqual(self.base.id, Base().id)
        self.assertNotEqual(self.base.id, Base(id=None).id)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(id=0).id, 0)
        self.assertEqual(Base(id=0.0).id, 0.0)
        self.assertEqual(Base(id="0").id, "0")
        self.assertEqual(Base(id=[0]).id, [0])
        self.assertEqual(Base(id={0}).id, {0})
        self.assertEqual(Base(id=(0, 0)).id, (0, 0))
        self.assertEqual(Base(id={0: 0}).id, {0: 0})

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Base(id=True).id, True)
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
        self.assertIsInstance(Base.create(), Base)
        self.assertIsInstance(Base.create(id=None), Base)
        self.assertIsInstance(Base.create(id=0), Base)
        self.assertIsInstance(Base.create(id=0.0), Base)
        self.assertIsInstance(Base.create(id="0"), Base)
        self.assertIsInstance(Base.create(id=(0,)), Base)
        self.assertIsInstance(Base.create(id=[0]), Base)
        self.assertIsInstance(Base.create(id={0}), Base)
        self.assertIsInstance(Base.create(id={0: 0}), Base)
        self.assertIsInstance(Base.create(id=True), Base)
        self.assertIsInstance(Base.create(id=type), Base)

    def test_create_id_equality(self):
        """Test the create method
        """
        self.assertNotEqual(self.base.id, Base.create().id)
        self.assertNotEqual(self.base.id, Base.create(id=None).id)
        self.assertEqual(Base.create(id=0).id, 0)
        self.assertEqual(Base.create(id=0.0).id, 0.0)
        self.assertEqual(Base.create(id="0").id, "0")
        self.assertEqual(Base.create(id=(0,)).id, (0,))
        self.assertEqual(Base.create(id=[0]).id, [0])
        self.assertEqual(Base.create(id={0}).id, {0})
        self.assertEqual(Base.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Base.create(id=True).id, True)
        self.assertIs(Base.create(id=type).id, type)
        self.assertIs(Base.create(id=None).id, None)

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
            Base.create, 0, 0
        )
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Base.create, 0
        )
