from textnode import *
import re
import pprint

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            while i < len(node.text):
                if node.text[i] == delimiter: #end of text before delimiter #just one character
                    new_list.append(TextNode(text, node.text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2 #advance a total of 2 for "**"
                    elif node.text[i] == "_":
                        i += 1

                    while node.text[i] != delimiter:
                        text += node.text[i]
                        i += 1

                    new_list.append(TextNode(text, text_type))
                    text = ""

                    if i+1 < len(node.text) and node.text[i] == "*" and node.text[i+1] == "*":
                        i += 2
                    elif node.text[i] == "_":
                        i += 1
                else:
                    text += node.text[i]
                    i += 1

            new_list.append(TextNode(text, node.text_type))
        else:
            new_list.append(node)
    return new_list

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

            pprint.pprint(new_list)
        elif text[i] == "_":
            new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC)
            i += 1
            while i < len(text) and text[i] != "_":
                i += 1
            i += 1
            
        else:
            i += 1



   

    return new_list
















def extract_markdown_images(text: str) -> list[tuple[str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            image_list: list[tuple[str]] = extract_markdown_images(node.text)

            while i < len(node.text):
                if node.text[i] != "!":
                    text += node.text[i]
                    i += 1
                elif node.text[i] == "!":
                    i += 1
                    while i < len(node.text) and node.text[i] != ")":
                        i += 1
                    i += 1
                    new_list.append(TextNode(text, node.text_type))
                    new_list.append(TextNode(image_list[0][0], TextType.IMAGE, image_list[0][1]))
                    text = ""

                    while i < len(node.text) and node.text[i] != "!":
                        text += node.text[i]
                        i += 1

                    new_list.append(TextNode(text, node.text_type))
                    new_list.append(TextNode(image_list[1][0], TextType.IMAGE, image_list[1][1]))
                    break
        else:
            raise Exception(f"TextType not TEXT. Does it need to be TEXT?")
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            link_list: list[tuple[str]] = extract_markdown_links(node.text)

            while i < len(node.text):
                if node.text[i] != "[":
                    text += node.text[i]
                    i += 1
                elif node.text[i] == "[":
                    i += 1
                    while i < len(node.text) and node.text[i] != ")":
                        i += 1
                    i += 1

                    new_list.append(TextNode(text, node.text_type))
                    new_list.append(TextNode(link_list[0][0], TextType.LINK, link_list[0][1]))
                    text = ""

                    while i < len(node.text) and node.text[i] != "[":
                        text += node.text[i]
                        i += 1

                    new_list.append(TextNode(text, node.text_type))
                    new_list.append(TextNode(link_list[1][0], TextType.LINK, link_list[1][1]))
                    break
        else:
            raise Exception("TextType not TEXT. Does it need to be TEXT?")
    return new_list

