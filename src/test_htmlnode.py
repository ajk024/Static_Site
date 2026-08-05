import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_6(self):
        props: dict[str] = {
            "href": "https://ww.google.com",
            "target": "_blank"
        }
        
        node = HTMLNode("p", "testing value", None, props)
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None, props)
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)

    def test_7(self):
        node = HTMLNode("p", "testing value", None)
        node_props = node.props_to_html()
        node2 = HTMLNode("p", "testing value", None)
        node2_props = node2.props_to_html()
        self.assertEqual(node_props, node2_props)

    def test_8(self):
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

    def test_9(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_10(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_11(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )



