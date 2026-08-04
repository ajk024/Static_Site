from textnode import *
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
                    new_list.append(TextNode(text, node.text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2 #advance a total of 2 for "**"
                    elif node.text[i] == "_" or node.text[i] == "`":
                        i += 1

                    while node.text[i] != delimiter:
                        text += node.text[i]
                        i += 1

                    new_list.append(TextNode(text, text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2
                    elif node.text[i] == "_" or node.text[i] == "`":
                        i += 1
                else:
                    text += node.text[i]
                    i += 1

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
        blocks[i] = blocks[i].strip("\n")
    return blocks