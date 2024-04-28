from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode


def main():
    tnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(tnode)

    node = HTMLNode(
        "a", "hehe", "", {"href": "https://www.google.com", "target": "_blank"}
    )
    print(node.props_to_html())
    print(node)

    tnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(tnode)
    print(text_node_to_html_node(tnode))

    tnode = TextNode("This is a test node", "link", "https://www.boot.dev")
    print(text_node_to_html_node(tnode))


main()
