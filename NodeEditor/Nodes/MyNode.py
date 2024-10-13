import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyNode(Node):
    def __init__(self):
        super().__init__(
            lable="My Node",
            type="Output",
            max_width=100,
            catagory="MyCategory"
        )
        # Add id for input field
        self.number_id = dpg.generate_uuid()
        
    def compose(self):
        # Add input field
        dpg.add_input_int(label="Number", default_value=0, tag=self.number_id, width=100)
        
    def execute(self, data: NodePackage) -> NodePackage:
        # Get value from input field
        number = dpg.get_value(self.number_id)
        # Add number to data
        data.number = number
        data.string = "Hello World"
        return data
    
    def on_save(self) -> dict:
        return {
            "number": dpg.get_value(self.number_id)
        }
        
    def on_load(self, data: dict):
        dpg.set_value(self.number_id, data["number"])