import unittest
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):

    def test_repr(self):
        node1 = HTMLNode(tag="<p>", value="Profound statement.",
                         props = {"href": "https://www.google.com", "target": "_blank"})
        test_string = node1.__repr__()
        expected_string = """tag = <p>, value = Profound statement., children = None, props = {'href': 'https://www.google.com', 'target': '_blank'}"""
        self.assertEqual(test_string, expected_string)

    def test_props_method(self):
        node1 = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        test_case1 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), test_case1)

    def test_props_none(self):
        node1 = HTMLNode(tag="<h1>", children=["h2", "h3"])
        test_case2 = None
        self.assertEqual(node1.props_to_html(), test_case2)

