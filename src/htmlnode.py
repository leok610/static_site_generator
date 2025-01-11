class HTMLNode():
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        # Props is meant to be a dictionary
        self.props = props

    def __repr__(self):
        return f'tag = <{self.tag}>, value = {self.value}, children = {self.children}, props = {self.props}'

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = f''
        if self.props:
            for k in self.props.keys():
                html_string += f' {k}="{self.props[k]}"'
            return html_string

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        if self.value == None:
            raise ValueError

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.props == None:
            tag_left, tag_right = f"<{self.tag}>", f"</{self.tag}>"
            return f"{tag_left}{self.value}{tag_right}"
        properties = self.props_to_html()
        tag_left, tag_right = f"<{self.tag}{properties}>", f"</{self.tag}>"
        return f"{tag_left}{self.value}{tag_right}"
