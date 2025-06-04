class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
 
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return "" 

        html = []
        props = self.props.items()
        for key, value in props:
            props_html = f'{key}="{value}"'
            html.append(props_html)
        return " " + " ".join(html)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag},value={self.value},children={self.children},props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag= tag, value= value, props= props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("All parent nodes must have a tag")
        