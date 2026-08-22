from textnode import *
from block_functions import *
import re
import pprint

def text_to_textnodes(text: str) -> list[TextNode]:
    new_list: list[TextNode] = [TextNode(text, TextType.TEXT)]
    i: int = 0

    while i < len(text):
        if i + 1 < len(text) and text[i] == "*" and text[i+1] == "*":
            new_list = split_nodes_delimiter(new_list, "*", TextType.BOLD)
            i += 2
            while i < len(text) and text[i] != "*":
                i += 1
            i += 2
        elif text[i] == "_":
            new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC)
            i += 1
            while i < len(text) and text[i] != "_":
                i += 1
            i += 1
        elif text[i] == "`":
            new_list = split_nodes_delimiter(new_list, "`", TextType.CODE)
            i += 1
            while i < len(text) and text[i] != "`":
                i += 1
            i += 1
        elif text[i] == "!": #image
            image_list: list[tuple[str]] = extract_markdown_images(text[i:]) #determine if there are valid images
      
            if len(image_list) > 0:
                new_list = split_nodes_image(new_list)
                while i < len(text) and text[i] != ")":
                    i += 1 
                i += 1
            else:
                i += 1
        elif text[i] == "[": #link
            link_list: list[tuple[str]] = extract_markdown_links(text[i:]) #determine if there are valid links

            if len(link_list) > 0:
                new_list = split_nodes_link(new_list)
                while i < len(text) and text[i] != ")":
                    i += 1
                i += 1
            else:
                i += 1
        else:
            i += 1
    return new_list

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            while i < len(node.text):
                if node.text[i] == delimiter: #end of text before delimiter #just one character
                    if text:
                        new_list.append(TextNode(text, node.text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2 #advance a total of 2 for "**"
                    elif node.text[i] == "_" or node.text[i] == "`":
                        i += 1

                    while node.text[i] != delimiter:
                        text += node.text[i]
                        i += 1

                    if text:
                        new_list.append(TextNode(text, text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2
                    elif node.text[i] == "_" or node.text[i] == "`":
                        i += 1
                else:
                    text += node.text[i]
                    i += 1

            if text:
                new_list.append(TextNode(text, node.text_type))
            i = 0
            text = ""
    return new_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        image_list: list[tuple[str]] = extract_markdown_images(node.text)

        if node.text_type != TextType.TEXT or len(image_list) == 0: #no properly formatted images
            new_list.append(node)
        else:
            while i < len(node.text):
                if node.text[i] == "!":
                    if len(text) > 0:
                        if text:
                            new_list.append(TextNode(text, node.text_type)) #text before image
                    new_list.append(TextNode(image_list[0][0], TextType.IMAGE, image_list[0][1])) #image

                    while i < len(node.text) and node.text[i] != ")":
                        i += 1
                    i += 1

                    if len(node.text[i:]) > 0: #text remaining in node
                        new_list.append(TextNode(node.text[i:], node.text_type)) #text after image
                    i = 0
                    text = ""
                    break  
                else:
                    text += node.text[i]
                    i += 1       
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        link_list: list[tuple[str]] = extract_markdown_links(node.text)

        if node.text_type != TextType.TEXT or len(link_list) == 0:
            new_list.append(node)
        else:
            while i < len(node.text):
                if node.text[i] == "[":
                    if len(text) > 0:
                        if text:
                            new_list.append(TextNode(text, node.text_type))
                    new_list.append(TextNode(link_list[0][0], TextType.LINK, link_list[0][1])) #link

                    while i < len(node.text) and node.text[i] != ")":
                        i += 1
                    i += 1

                    if len(node.text[i:]) > 0: #text remaining in node
                        new_list.append(TextNode(node.text[i:], node.text_type)) #text after image
                    i = 0
                    text = ""
                    break
                else:
                    text += node.text[i]
                    i += 1
    return new_list

def extract_markdown_images(text: str) -> list[tuple[str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")

    for i in range (len(blocks)):
        #strip "\n" and whitespace
        blocks[i] = blocks[i].strip("\n").strip()
    return blocks



def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    parent_nodes: list[ParentNode] = []

    for block in blocks:
        if not block: #block is empty
            continue

        block_type: BlockType = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children: list[LeafNode] = text_to_children(block.replace("\n", " "))
            parent_nodes.append(ParentNode("p", children))
        elif block_type == BlockType.CODE: #do not use text_to_textnodes b/c code should remain as-is
            leaf_node: LeafNode = text_node_to_html_node(TextNode(parse_code_block(block), TextType.CODE))
            parent_nodes.append(ParentNode("pre", [leaf_node]))
        elif block_type == BlockType.HEADING:
            heading_tag: str = parse_heading_tag(block)
            heading_value: str = parse_heading_value(block)
            children: list[LeafNode] = text_to_children(heading_value)
            parent_nodes.append(ParentNode(heading_tag, children))
        elif block_type == BlockType.QUOTE:
            quote_value: str = parse_quote_value(block)
            children: list[LeafNode] = text_to_children(quote_value)
            parent_nodes.append(ParentNode("blockquote", children))
        elif block_type == BlockType.UNORDERED_LIST:
            children: list[LeafNode] = text_to_children(parse_ul_block(block))
            parent_nodes.append(ParentNode("ul", children))
        elif block_type == BlockType.ORDERED_LIST:
            children: list[LeafNode] = text_to_children(parse_ol_block(block))
            parent_nodes.append(ParentNode("ol", children))
    html_node: ParentNode = ParentNode("div", parent_nodes)
    return html_node

def text_to_children(text: str) -> list[LeafNode]:
    leaf_node_list: list[LeafNode] = []

    for node in text_to_textnodes(text): #list of TextNode
        leaf_node: LeafNode = text_node_to_html_node(node)
        leaf_node_list.append(leaf_node)
    return leaf_node_list

def parse_code_block(text: str) -> str:
    code: str = ""

    #remove "```\n"
    for i in range (len(text)):
        if text[i] != "`":
            if text[i] == "\n" and text[i-1] == "`":
                pass
            else:
                code += text[i]
    return code

def parse_ul_block(text: str) -> str:
    new_str: str = ""

    for i in range(len(text)):
        if text[i] == "-":
            new_str += "<li>"
        elif text[i] == "\n":
            new_str += "</li>"
        elif text[i] == " " and text[i-1] == "-":
            pass
        else:
            new_str += text[i]
    new_str += "</li>"
    return new_str

def parse_ol_block(text: str) -> str:
    new_str: str = ""

    for i in range(len(text)):
        if text[i].isdigit():
            new_str += "<li>"
        elif text[i] == "\n":
            new_str += "</li>"
        elif text[i] == "." and text[i-1].isdigit():
            pass
        elif text[i] == " " and text[i-1] == ".":
            pass
        else:
            new_str += text[i]
    new_str += "</li>"
    return new_str

def parse_quote_value(text: str) -> str: #return quote value without markdown formatting
    value: str = ""
    for i in range (len(text)):
        if text[i] == ">":
            pass
        elif text[i] == " " and text[i-1] == ">":
            pass
        else:
            value += text[i]
    return value

def parse_heading_tag(text: str) -> str: #return heading tag
    i: int = 0
    while text[i] != " ":
        i += 1
    return f"h{i}"

def parse_heading_value(text: str) -> str: #return heading value without markdown formatting
    value: str = ""
    i = 0
    while i < len(text) and text[i] != " ":
        i += 1
    i += 1
    while i < len(text):
        value += text[i]
        i += 1
    return value
            
