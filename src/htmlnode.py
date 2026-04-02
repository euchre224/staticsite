

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        conv_list = []
        for i in self.props:
            conv_list.append(f'{i}="{self.props[i]}"')
        return " ".join(conv_list)


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__()


    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
        

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
