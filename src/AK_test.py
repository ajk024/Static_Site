import sys
import pprint
from htmlnode import *
from textnode import *
from functions import *
from block_functions import *
#from ..src import *

test_num: int = 11

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
    print(node)
    print(node.text)
    #html_node = text_node_to_html_node(node)
    #print(html_node)
    #print(html_node.to_html())
    """
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

    
    node = TextNode("Testing link node", TextType.LINK)
    html_node = text_node_to_html_node(node)
    print(html_node)
    

    node = TextNode("Testing image node", TextType.IMAGE, "www.image.com")
    html_node = text_node_to_html_node(node)
    print(html_node)
    print(html_node.to_html())
    """

elif test_num == 2:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

elif test_num == 3:
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

elif test_num == 4:
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    node = TextNode(text, TextType.TEXT)
    a = split_nodes_image([node])
    #pprint.pprint(a, width=1)

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    node = TextNode(text, TextType.TEXT)
    a = split_nodes_link([node])
    pprint.pprint(a, width=1)
   
elif test_num == 5:
    text_1 = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_2 = "This is **bold** and some _italic_ and more **second bold** and here is some `code block` and even more **bold** text here."
    text_3 = "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_4 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    text_5 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

    text = text_4 + text_1 + text_3 + text_5 + text_2

    a = text_to_textnodes(text)
    pprint.pprint(a)

elif test_num == 6:
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

    a = markdown_to_blocks(md)
    print(a)

elif test_num == 7:
    md = """```
some code here
```
"""
    a = block_to_block_type(md)
    print(a)

elif test_num == 8: #unordered list
    md = """- Item 1
- Item 2
- Item 3
- Item 4
"""
    a = block_to_block_type(md)
    print(a)

    md = """- Item 1
- Item 2
- Item 3
-
"""
    a = block_to_block_type(md)
    print(a)

elif test_num == 9: #ordered list
    md = """1. Item 1
2. Item 2
3. Item 3
"""
    a = block_to_block_type(md)
    print(a)

elif test_num == 10: 
    md = """
This is **bolded** paragraph
text in a p
tag here


This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

elif test_num == 11:
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(md)