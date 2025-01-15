import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class Test_HTMLNodeClass(unittest.TestCase):

    def test_repr(self):
        node1 = HTMLNode(tag="p", value="Profound statement.",
                         props = {"href": "https://www.google.com", "target": "_blank"})
        test_string = node1.__repr__()
        expected_string = """tag = <p>, value = Profound statement., children = None, props = {'href': 'https://www.google.com', 'target': '_blank'}"""
        self.assertEqual(test_string, expected_string)

    def test_props_method(self):
        node1 = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        test_case1 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), test_case1)

    def test_props_none(self):
        node1 = HTMLNode(tag="h1", children=["h2", "h3"])
        test_case2 = None
        self.assertEqual(node1.props_to_html(), test_case2)

    def test_leaf_init(self):
        node1 = LeafNode(tag="p", value="hello world")
        test_case1 = "tag = <p>, value = hello world, children = None, props = None"
        self.assertEqual(repr(node1), test_case1)

class Test_LeafNodeClass(unittest.TestCase):

    # Leaf nodes must have a value
    def test_leaf_require_value(self):
        self.assertRaises(ValueError, LeafNode, tag="p")

    # Leaf nodes cannot have child nodes
    def test_leaf_no_children(self):
        self.assertRaises(TypeError, LeafNode, tag="p", value="hello", children="joe")

    # Leaf nodes return a raw string with .to_html method if there is no tag
    def test_leaf_html_no_tag(self):
        node1 = LeafNode(value="hello")
        self.assertEqual(node1.to_html(), "hello")

    # Test leaf node HTML with no props
    def test_leaf_html_no_props(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")

    # Test leaf node HTML with single property
    def test_leaf_html_props1(self):
        node1 = LeafNode("a", "Click me!", {"href":"https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')

    # Test leaf node HTML with two properties
    def test_leaf_html_props1(self):
        properties = {"href":"https://www.google.com", "id": "weird"}
        node1 = LeafNode("a", "Click me!", properties)
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com" id="weird">Click me!</a>')

class Test_ParentNodeClass(unittest.TestCase):
    def setUp(self):
        self.properties = {"href":"https://www.google.com", "id": "weird"}
        self.node1 = LeafNode("a", "Click me!", self.properties)

    # Parent node requires a tag
    def test_parent_has_tag(self):
        self.assertRaises(TypeError, ParentNode, children = self.node1)

    # Parent node requires children
    def test_parent_has_children(self):
        self.assertRaises(TypeError, ParentNode, tag = "b")
        
    # Parent node may not have a value argument
    def test_parent_has_no_value(self):
        node2 = LeafNode("a", "Click me!")
        self.assertRaises(TypeError, ParentNode, tag = "b", children = [node2],
                          value = "hello world")

    # Parent node may have optional props parameter
    def test_parent_has_optional_props(self):
        p = ParentNode("b", [self.node1], self.properties)
        self.assertEqual(self.properties, p.props)

    # Parent node html raises ValueError if no tag is present
    def test_parent_html_has_tag(self):
        p = ParentNode("b", [self.node1])
        p.tag = None
        with self.assertRaises(ValueError, msg="Value error about tags") as test:
            p.to_html()
        exception = test.exception
        self.assertEqual("Parent nodes must have tags",exception.args[0])

    # Parent node html raises ValueError if no children are present
    def test_parent_html_has_children(self):
        p = ParentNode("b", [self.node1])
        p.children = None
        with self.assertRaises(ValueError, msg="different error from tag") as test:
            p.to_html()
        exception = test.exception
        self.assertEqual("Parent nodes must have children",exception.args[0])

    def test_parent_html_tag_format(self):
        p = ParentNode("p", [self.node1])
        output = p.to_html()
        self.assertEqual(output[0:3], "<p>")
        self.assertEqual(output[-4:], "</p>")

    def test_parent_html_has_valid_children_list(self):
        p = ParentNode("p", "hello")
        with self.assertRaises(TypeError) as test:
            p.to_html()
        exception = test.exception
        self.assertEqual("Children must be list of at least one member", exception.args[0])
