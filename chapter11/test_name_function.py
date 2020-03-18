import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated_name = get_formatted_name('alice','john')
        self.assertEqual(formated_name,"Alice John")

unittest.main