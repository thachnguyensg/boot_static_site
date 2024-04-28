class HTMLNode:
    def __init__(self, tag, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        ):
            return True
        return False

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""
        if not self.props:
            return props_str
        for prop in self.props:
            props_str += f' {prop}="{self.props[prop]}"'
        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
        # return f"HTMLNode(tag: {self.tag}, value: {self.value}, props: {self.props}, children: {self.children})"
