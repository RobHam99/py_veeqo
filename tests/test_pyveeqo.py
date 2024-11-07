import unittest
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.endpoints import *

class TestPyVeeqo(unittest.TestCase):
    _TEST_URL = "https://private-anon-54bd4df4a1-veeqo.apiary-mock.com/"
    
    def test_key_none(self):
        """Raise an error when a key has not been given.
        """
        try:
            PyVeeqo()
            self.fail('A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)