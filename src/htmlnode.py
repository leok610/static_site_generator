class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}'

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = f''
        if self.props:
            for k in self.props.keys():
                html_string += f' {k}="{self.props[k]}"'
            return html_string

node1 = HTMLNode(tag="<p>", value="Profound statement.",
                         props = {"href": "https://www.google.com", "target": "_blank"})

