import unittest
from block_functions import *

class TestBlockFunctions(unittest.TestCase):
    def test_block_func_1(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("### Heading 3"))

    def test_block_func_2(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("# Heading 1"))


if __name__ == "__main__":
    unittest.main()