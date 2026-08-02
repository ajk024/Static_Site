from __future__ import annotations
from enum import Enum
from htmlnode import *


class TextType(Enum):
    TEXT = "raw text"
    BOLD = "bold" #**
    ITALIC = "italic" #_
    CODE = "code text" #```
    LINK = "link" #[]()
    IMAGE = "image" #![]()
    

class TextNode:
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode):
        if isinstance(other, TextNode):
            return(
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise Exception("text_node text_type not in TextType")

    if text_node.text_type == TextType.TEXT:
        new_leaf = LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        new_leaf = LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        new_leaf = LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        new_leaf = LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise Exception("LINK TextType requires a url.")
        prop: dict[str] = {
            "href": text_node.url
        }
        new_leaf = LeafNode("a", text_node.text, prop)
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise Exception("IMAGE TextType requires a url.")
        prop: dict[str] = {
            "src": text_node.url,
            "alt": text_node.text
        }
        new_leaf = LeafNode("img", text_node.text, prop)
    return new_leaf

    