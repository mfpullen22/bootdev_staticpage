import unittest

from htmlnode import LeafNode, ParentNode, HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNode("span", "This is a span", None, {"class": "container"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=This is a div, children=None, props={'class': 'container'})")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "first child")
        child2 = LeafNode("span", "second child")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>first child</span><span>second child</span></div>",
        )

    def test_to_html_with_mixed_children(self):
        leaf_child = LeafNode("b", "bold text")
        parent_child = ParentNode("p", [LeafNode("i", "italic text")])
        parent_node = ParentNode("div", [leaf_child, parent_child])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>bold text</b><p><i>italic text</i></p></div>",
        )

    def test_to_html_with_no_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")]).to_html()

    def test_to_html_with_empty_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("", [LeafNode("span", "child")]).to_html()

    def test_to_html_with_no_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_to_html_with_empty_children_list(self):
        # Empty list should be valid, just no children rendered
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_multiple_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(
            "div", 
            [child_node], 
            {"class": "container", "id": "main", "data-test": "true"}
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main" data-test="true"><span>child</span></div>',
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_eq(self):
        node = LeafNode("div", "This is a div", {"class": "container"})
        node2 = LeafNode("div", "This is a div", {"class": "container"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("div", "This is a div", {"class": "container"})
        node2 = LeafNode("span", "This is a span", {"class": "container"})
        self.assertNotEqual(node, node2)

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"