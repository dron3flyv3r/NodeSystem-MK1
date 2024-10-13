import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyOtherNode(Node):
    
    def __init__(self):
        super().__init__(
            lable="My Other Node",
            type="Input",
            max_width=100,
            catagory="MyCategory"
        )
        
        # Add id for input field
        self.text_id = dpg.generate_uuid()
        
    def compose(self):
        # Add input field
        dpg.add_text("Text", tag=self.text_id)
        
    def execute(self, data: NodePackage) -> NodePackage:
        dpg.set_value(self.text_id, data.text())
        return data