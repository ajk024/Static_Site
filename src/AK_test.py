import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from htmlnode import *
from textnode import *
from functions import *

test_num: int = 3

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

elif test_num == 2:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

elif test_num == 3:
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    
   
    