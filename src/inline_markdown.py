import re

from textnode import (
    TextNode,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if len(old_nodes) < 1:
        return new_nodes

    for oldnode in old_nodes:
        if not oldnode.text_type == text_type_text:
            new_nodes.append(oldnode)
        else:
            nodes = __split_node(oldnode.text.split(delimiter), delimiter, text_type)
            if nodes:
                new_nodes.extend(nodes)

    return new_nodes


def __split_node(inputs, delimiter, text_type):
    if len(inputs) % 2 == 0:
        raise ValueError(f"Invalid syntax, missing closing {delimiter}")

    nodes = []
    for i in range(len(inputs)):
        if not inputs[i] == "":
            if i % 2 == 0:
                nodes.append(TextNode(inputs[i], text_type_text))
            else:
                nodes.append(TextNode(inputs[i], text_type))

    return nodes


# Cursed
def __split_node_darkside(inputs, delimiter, text_type, outputs):
    if len(inputs) == 0:
        return outputs
    if len(inputs) == 1:
        if not inputs[0] == "":
            outputs.append(TextNode(inputs[0], text_type_text))
        return outputs

    if len(inputs) % 2 == 0:
        raise ValueError(f"Invalid syntax, missing closing {delimiter}")

    if not inputs[0] == "":
        outputs.append(TextNode(inputs[0], text_type_text))
    if not inputs[1] == "":
        outputs.append(TextNode(inputs[1], text_type))
    return __split_node_darkside(inputs[2:], delimiter, text_type, outputs)


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches
