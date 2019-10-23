#!/usr/bin/python3
"""Provides unittest for the 'Square' class provided by the 'models' module
"""

import unittest
import json
from os import chdir, getcwd, path, remove
from shutil import rmtree
from tempfile import mkdtemp

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test square model methods
    """
    def setUp(self):
        """Create a temporary directory and Base instance
        """
        self.square = Square(1)
        chdir(mkdtemp())

    def tearDown(self):
        """Remove temporary files and directories
        """
        rmtree(getcwd(), ignore_errors=True)

    def test_square(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.square, Square)
        self.assertIsInstance(self.square, Base)

    def test_square_width(self):
        """Test the __init__ method
        """
        self.assertEqual(self.square.width, 1)

    def test_square_height(self):
        """Test the __init__ method
        """
        self.assertEqual(self.square.height, 1)

    def test_square_x(self):
        """Test the __init__ method
        """
        self.assertEqual(self.square.x, 0)

    def test_square_y(self):
        """Test the __init__ method
        """
        self.assertEqual(self.square.y, 0)

    def test_square_id(self):
        """Test the __init__ method
        """
        self.assertIsInstance(self.square.id, int)
        self.assertGreater(self.square.id, 0)

    def test_init_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Square(1), Square)
        self.assertIsInstance(Square(1, id=None), Square)
        self.assertIsInstance(Square(1, 0, 0), Square)
        self.assertIsInstance(Square(1, 0, 0, 0), Square)
        self.assertIsInstance(Square(1, id=0), Square)
        self.assertIsInstance(Square(1, id=0.0), Square)
        self.assertIsInstance(Square(1, id="0"), Square)
        self.assertIsInstance(Square(1, id=(0,)), Square)
        self.assertIsInstance(Square(1, id=[0]), Square)
        self.assertIsInstance(Square(1, id={0}), Square)
        self.assertIsInstance(Square(1, id={0: 0}), Square)
        self.assertIsInstance(Square(1, id=True), Square)
        self.assertIsInstance(Square(1, id=type), Square)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        self.assertNotEqual(self.square.id, Square(1).id)
        self.assertNotEqual(self.square.id, Square(1, id=None).id)
        self.assertEqual(Square(1, 1, 1, 0).id, 0)
        self.assertEqual(Square(1, id=0.0).id, 0.0)
        self.assertEqual(Square(1, id="0").id, "0")
        self.assertEqual(Square(1, id=[0]).id, [0])
        self.assertEqual(Square(1, id={0}).id, {0})
        self.assertEqual(Square(1, id=(0, 0)).id, (0, 0))
        self.assertEqual(Square(1, id={0: 0}).id, {0: 0})

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Square(1, id=True).id, True)
        self.assertIs(Square(1, id=type).id, type)

    def test_init_id_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Square(1).id, int)
        self.assertIsInstance(Square(1, id=None).id, int)

    def test_init_raises(self):
        """Test the __init__ method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) missing 1 required positional argument\\b.*",
            Square
        )

    def test_create_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create(), Square)
        self.assertIsInstance(Square.create(id=None), Square)
        self.assertIsInstance(Square.create(id=0), Square)
        self.assertIsInstance(Square.create(id=0.0), Square)
        self.assertIsInstance(Square.create(id="0"), Square)
        self.assertIsInstance(Square.create(id=(0,)), Square)
        self.assertIsInstance(Square.create(id=[0]), Square)
        self.assertIsInstance(Square.create(id={0}), Square)
        self.assertIsInstance(Square.create(id={0: 0}), Square)
        self.assertIsInstance(Square.create(id=True), Square)
        self.assertIsInstance(Square.create(id=type), Square)

    def test_create_id_equality(self):
        """Test the create method
        """
        self.assertNotEqual(self.square.id, Square.create().id)
        self.assertNotEqual(self.square.id, Square.create(id=None).id)
        self.assertEqual(Square.create(id=0).id, 0)
        self.assertEqual(Square.create(id=0.0).id, 0.0)
        self.assertEqual(Square.create(id="0").id, "0")
        self.assertEqual(Square.create(id=(0,)).id, (0,))
        self.assertEqual(Square.create(id=[0]).id, [0])
        self.assertEqual(Square.create(id={0}).id, {0})
        self.assertEqual(Square.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Square.create(id=True).id, True)
        self.assertIs(Square.create(id=type).id, type)
        self.assertIs(Square.create(id=None).id, None)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create().id, int)

    def test_create_raises(self):
        """Test the create method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Square.create, 0
        )

    def test_save_to_file(self):
        """Test the save_to_file method
        """
        types = (int, float, str, tuple, list, dict, bool)
        insts = [self.square] + [Square(1, id=t()) for t in types]
        fname = 'Square.json'
        try:
            remove(fname)
        except FileNotFoundError:
            pass
        self.assertIsNone(Square.save_to_file(None))
        with open(fname) as ifile:
            self.assertEqual(ifile.read(), '[]')
        for index in range(len(insts)):
            self.assertIsNone(Square.save_to_file(insts[index:]))
            with open(fname) as ifile:
                self.assertEqual(ifile.read(), Square.to_json_string(
                    [obj.to_dictionary() for obj in insts[index:]]
                ))
