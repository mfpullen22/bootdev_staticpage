import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
    
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, link, http://example.com)")
    
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "http://example.com")
        self.assertEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()