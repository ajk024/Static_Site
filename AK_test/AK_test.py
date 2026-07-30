import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.htmlnode import *
from src.textnode import *

test_num: int = 0

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
    #node = TextNode("Testing text node", TextType.TEXT)
    ...