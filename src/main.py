from textnode import TextType, TextNode

print("hello world")

def main():
    TEXT = "This is some anchor text"
    TEXT_TYPE = "link"
    URL = "https://www.boot.dev"
    test = TextNode(TEXT, TEXT_TYPE, URL)
    # otra = TextNode(TEXT, "bold", URL)
    otra = TextNode(TEXT, TEXT_TYPE, URL)
    print(test.__eq__(otra))
    print(test)

main()