import unittest
from block_functions import *
from functions import markdown_to_blocks

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

    def test_20(self):
        text  = """- Item 1
- Item 2
- Item 3
- Item 4
"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(text))

    def test_21(self):
        md = """- Item 1
- Item 2
- Item 3
-Item 4
"""
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_22(self):
        md = """- Item 1
- Item 2
- Item 3
*
"""
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_23(self):
        md = """1. Item 1
2. Item 2
3. Item 3
"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(md))

    def test_24(self):
        md = """1. Item 1
2. Item 2
6. Item 3
"""
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_25(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        answer = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        
        self.assertEqual(answer, markdown_to_blocks(md))

    def test_26(self):
        md = """
     This is **bolded** paragraph

  This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

               - This is a list
- with items
"""

        answer = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        
        self.assertEqual(answer, markdown_to_blocks(md))

    def test_27(self):
        md = "This is a normal paragraph!"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))
        



