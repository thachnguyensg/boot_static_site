import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
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


def split_nodes_image(old_nodes):
    return __split_link_image(old_nodes, text_type_image)


def split_nodes_link(old_nodes):
    return __split_link_image(old_nodes, text_type_link)


def __split_link_image(old_nodes, text_type):
    new_nodes = []
    if len(old_nodes) < 1:
        return new_nodes

    for oldnode in old_nodes:
        text = oldnode.text
        extracted_items = []
        if text_type == text_type_image:
            extracted_items = extract_markdown_images(text)
        else:
            extracted_items = extract_markdown_links(text)

        for item in extracted_items:
            delimiter = ""
            if text_type == text_type_image:
                delimiter = f"![{item[0]}]({item[1]})"
            else:
                delimiter = f"[{item[0]}]({item[1]})"

            nodes = text.split(delimiter, 1)
            if not nodes[0] == "":
                new_nodes.append(TextNode(nodes[0], text_type_text))
            new_nodes.append(TextNode(item[0], text_type, item[1]))
            text = nodes[1]

        if not text == "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes
