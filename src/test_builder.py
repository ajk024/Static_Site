import unittest
from builder import *

class TestBuilder(unittest.TestCase):
    def test_33(self):
        md = "# HELLO"
        self.assertEqual("HELLO", extract_title(md))

    def test_34(self):
        md = """
# HELLO HERE       
more stuff
"""
        self.assertEqual("HELLO HERE", extract_title(md))