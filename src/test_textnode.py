import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_2(self):
        node = TextNode("Testing a text node", TextType.ITALIC)
        node2 = TextNode("Testing a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_3(self):
        node = TextNode("Testing a text node", TextType.LINK, "www.world.com")
        node2 = TextNode("Testing a text node", TextType.LINK, "www.world.com")
        self.assertEqual(node, node2)

    def test_4(self):
        node = TextNode("Testing a text node", TextType.ITALIC, None)
        node2 = TextNode("Testing a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_5(self):
        node = TextNode("Testing a text node", TextType.ITALIC, None)
        node2 = TextNode("Testing a text node", TextType.LINK, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()