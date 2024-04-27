from textnode import TextNode
from htmlnode import HTMLNode


def main():
    tnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(tnode)

    node = HTMLNode(
        "a", "hehe", "", {"href": "https://www.google.com", "target": "_blank"}
    )
    print(node.props_to_html())
    print(node)


main()
