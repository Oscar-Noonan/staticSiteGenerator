import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is some example text", None,
                        {"href": "https://www.google.com", "target": "_blank",})
        node_as_string: str = repr(node)
        self.assertEqual(node_as_string,
                         'HTMLNode(p, This is some example text, None, href="https://www.google.com" target="_blank")')

    def test_props_to_html(self):
            node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "style": "color:red;",})
            self.assertEqual(node.props_to_html(), 'href="https://www.boot.dev" style="color:red;"')

    def test_props_to_html2(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()