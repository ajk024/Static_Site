import unittest
from block_functions import *

class TestBlockFunctions(unittest.TestCase):
    def test_15(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("### Heading 3"))

    def test_16(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("# Heading 1"))

    def test_17(self):
        md = """```
some code here
```
"""
        self.assertEqual(BlockType.CODE, block_to_block_type(md))

    def test_18(self):
        md = """```
some code here
`
"""
        #self.assertRaises(Exception, block_to_block_type, md)
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_19(self):
        text = "> My quote here"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))



