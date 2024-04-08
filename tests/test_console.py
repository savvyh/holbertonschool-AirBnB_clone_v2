#!/usr/bin/python3
""" """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestDoCreate(unittest.TestCase):
    """Test cases for the do_create method of the console."""

    def setUp(self):
        """Set up for the tests."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up tasks."""
        all_objs = storage.all()
        for key in list(all_objs.keys()):
            del all_objs[key]
        storage.save()

    def test_create_no_class(self):
        """Test do_create with no class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_create_invalid_class(self):
        """Test do_create with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_create_no_params(self):
        """Test do_create with valid class name but no additional param."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            # Output should be the id of the created object
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_create_with_params(self):
        """Test do_create with valid class name and parameters."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create BaseModel name="My_little_house"')
            new_id = f.getvalue().strip()
            new_obj = storage.all()['BaseModel.' + new_id]
            self.assertEqual(new_obj.name, "My little house")


if __name__ == "__main__":
    unittest.main()
