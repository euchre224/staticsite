import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_tag = "p"
        test_value = "this is test text"
        test_children = []
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(test_tag, test_value, test_children, test_props)
        node2 = HTMLNode("p", test_value, None, test_props)
        node3 = HTMLNode("p", test_value, test_children)
        node4 = HTMLNode()
        # print("woo")
        node.to_html
        node2.to_html
        node3.to_html
        node4.to_html
        node.props_to_html
        node2.props_to_html
        node3.props_to_html
        node4.props_to_html
        
        # print("boo")
        print(node)



if __name__ == "__main__":
    unittest.main()