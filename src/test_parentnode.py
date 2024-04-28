import unittest

from htmlnode import ParentNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

        node = ParentNode("p", [ParentNode("div", [LeafNode(None, "Text")])])
        self.assertEqual(node.to_html(), "<p><div>Text</div></p>")

        node = ParentNode(
            "p",
            [
                ParentNode("div", [LeafNode(None, "Text")]),
                ParentNode("div", [LeafNode(None, "Text2")]),
            ],
        )
        self.assertEqual(node.to_html(), "<p><div>Text</div><div>Text2</div></p>")

        node = ParentNode(
            "p",
            [
                ParentNode("div", [LeafNode(None, "Text")]),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Text2"),
                        ParentNode("p", [LeafNode(None, "Para")]),
                    ],
                ),
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><div>Text</div><div>Text2<p>Para</p></div></p>"
        )


if __name__ == "__main__":
    unittest.main()
