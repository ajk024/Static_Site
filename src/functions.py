from textnode import *
import re

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    new_list: list[TextNode] = []
    text: str = ""
    i: int = 0

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            while i < len(node.text):
                if node.text[i] == delimiter: #end of text before delimiter
                    new_list.append(TextNode(text, node.text_type))
                    text = ""
                    i += 1

                    while node.text[i] != delimiter:
                        text += node.text[i]
                        i += 1

                    new_list.append(TextNode(text, text_type))
                    text = ""
                    i += 1

                else:
                    text += node.text[i]
                    i += 1
            if text == node.text_type: #delimiter not found
                raise Exception(f"Delimiter not found in text.")
            else:
                new_list.append(TextNode(text, node.text_type))
        else:
            new_list.append(node)

    return new_list

def extract_markdown_images(text: str) -> list[tuple[str]]:
    alt_matches = re.findall(r"\[(.*?)\]", text)
    url_matches = re.findall(r"\((.*?)\)", text)
    print(alt_matches)
    print(url_matches)
    matches = list(zip(alt_matches, url_matches))

    return matches