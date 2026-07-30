import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from htmlnode import *
from textnode import *

test_num: int = 1

if test_num == 0:
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )



    a = node.to_html()
    print(a)
    #print(type(node))
    #print(type(node).__name__)

elif test_num == 1:
    node = TextNode("Testing text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())

    node = TextNode("Testing bold node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())

    node = TextNode("Testing code node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())

    node = TextNode("Testing link node", TextType.LINK, "www.boot.dev")
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())

    """
    node = TextNode("Testing link node", TextType.LINK)
    html_node = text_node_to_html_node(node)
    print(html_node)
    """

    node = TextNode("Testing image node", TextType.IMAGE, "www.image.com")
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())

    