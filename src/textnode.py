from enum import Enum

class TextType(Enum):
    PLAIN_TEXTTYPE = "plain"
    BOLD_TEXTTYPE = "bold"
    ITALIC_TEXTTYPE = "italic"
    CODE_TEXTTYPE = "code"
    LINK_TEXTTYPE = "link"
    IMAGETEXTTYPE = "image"

class TextNode():

    def __init__(self, TEXT, TEXT_TYPE, URL):
        self.text = TEXT
        self.text_type = TextType(TEXT_TYPE)
        self.url = URL
        self.items = [self.text, self.text_type, self.url]

    def __eq__(self, other):
        for i in range(len(self.items)):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"