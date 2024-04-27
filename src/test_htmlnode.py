import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hehe")
        node2 = HTMLNode("p", "hehe")
        self.assertEqual(node, node2)

        node = HTMLNode(
            "a", "hehe", {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(
            "a", "hehe", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node, node2)

        node = HTMLNode(
            "a", "hehe", "", {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(
            "a", "", "", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertNotEqual(node, node2)

        node = HTMLNode("p", "hehe")
        node2 = HTMLNode("p", "hehe")
        self.assertEqual(node.props_to_html(), node2.props_to_html())

        node = HTMLNode(
            "a", "hehe", "", {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(
            "a", "", "", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), node2.props_to_html())


if __name__ == "__main__":
    unittest.main()
