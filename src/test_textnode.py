import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        # print("woo")
        self.assertEqual(node, node2)
        # print("boo")
        self.assertNotEqual(node, node3)
        self.assertEqual(node.url, None)
        self.assertNotEqual(node3.url, None)
        self.assertEqual(node.text_type, node2.text_type)
        self.assertNotEqual(node.text_type, node3.text_type)

    # def assertEqual(self, node, node2):
    #     if node == node2:
    #         return True
    #     else:
    #         return False

    # def assertNotEqual(self, node, node2):
    #     if node != node2:
    #         return True
    #     else:
    #         return False


if __name__ == "__main__":
    unittest.main()