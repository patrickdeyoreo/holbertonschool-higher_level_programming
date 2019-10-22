#!/usr/bin/python3
"""Provides unittest for the 'Rectangle' class provided by the 'models' module
"""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test rectangle model methods
    """
    def setUp(self):
        self.rectangle = Rectangle(1, 1)

    def test_rectangle(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.rectangle, Rectangle)

    def test_rectangle_width(self):
        """Test the __init__ method
        """
        self.assertEqual(self.rectangle.width, 1)

    def test_rectangle_height(self):
        """Test the __init__ method
        """
        self.assertEqual(self.rectangle.height, 1)

    def test_rectangle_x(self):
        """Test the __init__ method
        """
        self.assertEqual(self.rectangle.x, 0)

    def test_rectangle_y(self):
        """Test the __init__ method
        """
        self.assertEqual(self.rectangle.y, 0)

    def test_rectangle_id(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.rectangle.id, int)
        self.assertGreater(self.rectangle.id, 0)

    def test_init_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Rectangle(1, 1), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=None), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, 0, 0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, 0, 0, 0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=0.0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id="0"), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=(0,)), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=[0]), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id={0}), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id={0: 0}), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=True), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=type), Rectangle)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        self.assertNotEqual(self.rectangle.id, Rectangle(1, 1).id)
        self.assertNotEqual(self.rectangle.id, Rectangle(1, 1, id=None).id)
        self.assertEqual(Rectangle(1, 1, 1, 1, 0).id, 0)
        self.assertEqual(Rectangle(1, 1, id=0.0).id, 0.0)
        self.assertEqual(Rectangle(1, 1, id="0").id, "0")
        self.assertEqual(Rectangle(1, 1, id=[0]).id, [0])
        self.assertEqual(Rectangle(1, 1, id={0}).id, {0})
        self.assertEqual(Rectangle(1, 1, id=(0, 0)).id, (0, 0))
        self.assertEqual(Rectangle(1, 1, id={0: 0}).id, {0: 0})

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Rectangle(1, 1, id=True).id, True)
        self.assertIs(Rectangle(1, 1, id=type).id, type)

    def test_init_id_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Rectangle(1, 1).id, int)
        self.assertIsInstance(Rectangle(1, 1, id=None).id, int)

    def test_init_raises(self):
        """Test the __init__ method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) missing 2 required positional arguments\\b.*",
            Rectangle
        )
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) takes from 3 to 6 positional arguments\\b.*",
            Rectangle, 0, 0, 0, 0, 0, 0
        )

    def test_create_type(self):
        """Test the create method
        """
        self.assertIsInstance(Rectangle.create(), Rectangle)
        self.assertIsInstance(Rectangle.create(id=None), Rectangle)
        self.assertIsInstance(Rectangle.create(id=0), Rectangle)
        self.assertIsInstance(Rectangle.create(id=0.0), Rectangle)
        self.assertIsInstance(Rectangle.create(id="0"), Rectangle)
        self.assertIsInstance(Rectangle.create(id=(0,)), Rectangle)
        self.assertIsInstance(Rectangle.create(id=[0]), Rectangle)
        self.assertIsInstance(Rectangle.create(id={0}), Rectangle)
        self.assertIsInstance(Rectangle.create(id={0: 0}), Rectangle)
        self.assertIsInstance(Rectangle.create(id=True), Rectangle)
        self.assertIsInstance(Rectangle.create(id=type), Rectangle)

    def test_create_id_equality(self):
        """Test the create method
        """
        self.assertNotEqual(self.rectangle.id, Rectangle.create().id)
        self.assertNotEqual(self.rectangle.id, Rectangle.create(id=None).id)
        self.assertEqual(Rectangle.create(id=0).id, 0)
        self.assertEqual(Rectangle.create(id=0.0).id, 0.0)
        self.assertEqual(Rectangle.create(id="0").id, "0")
        self.assertEqual(Rectangle.create(id=(0,)).id, (0,))
        self.assertEqual(Rectangle.create(id=[0]).id, [0])
        self.assertEqual(Rectangle.create(id={0}).id, {0})
        self.assertEqual(Rectangle.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Rectangle.create(id=True).id, True)
        self.assertIs(Rectangle.create(id=type).id, type)
        self.assertIs(Rectangle.create(id=None).id, None)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Rectangle.create().id, int)

    def test_create_raises(self):
        """Test the create method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Rectangle.create, 0
        )
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Rectangle.create, 0, 0
        )
