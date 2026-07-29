import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props: dict[str] = {
            "href": "https://ww.google.com",
            "target": "_blank"
        }
        
        node = HTMLNode("p", "testing value", None, props)
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None, props)
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)

    def test_props_to_html_1(self):
        node = HTMLNode("p", "testing value", None)
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None)
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)

    def test_props_to_html_2(self):
        node = HTMLNode("p", "testing value", None, "")
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None, "")
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)
    """
    def test_props_to_html(self): #raises TypeError
        props = [
            "href https://ww.google.com",
            "target _blank"
        ]
        
        node = HTMLNode("p", "testing value", None, props)
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None, props)
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)
    """

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


