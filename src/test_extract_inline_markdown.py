import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image 1](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image 1", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
