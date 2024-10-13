# Node Editor System

This is a simple node editor system that I made for a project. It is a simple system that allows you to create nodes and connect them together. The nodes can be of different types and can be connected to each other in a specific way.

## Features
- Easy to create new nodes
- Auto node import from a folder
- Auto save and load projects
- Simple and basic node configuration
- Save and load node projects

## How to use
Clone the repository
```sh
git clone https://github.com/dron3flyv3r/NodeSystem-MK1.git
```

Install the dependencies
```sh
pip install -r requirements.txt
```

Create a new node by making a new file in the `nodes` folder. The name of the file **MUST** be the same as the name of the class.
```sh
touch NodeEditor/Nodes/MyNode.py
```

Modify the `NodePackage` class in the `NodeEditor/Core/NodePackage.py` file. The reason for this is so the entire node system becomes type safe. You can also add functions to the `NodePackage` class to make to process data or do operations on the nodes.
```python
class NodePackage:
    # Define the variables that the node package will have
    number: int
    string: str
    
    # Make functions that will be used to process the data (optional)
    def text(self) -> str:
        return f"{self.number}. {self.string}"

    def copy(self) -> 'NodePackage':
        new_package = NodePackage()
        for key, value in self.__dict__.items():
            setattr(new_package, key, copy.deepcopy(value))
        return new_package

```

Create a new class that inherits from the `Node` class.
```python
import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyNode(Node):
    def __init__(self):
        super().__init__(
            lable="My Node",
            type="Output",
            max_width=300,
            catagory="MyCategory"
        )
```

(Optional) Create some user input fields for the node.
```python
import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyNode(Node):
    def __init__(self):
        super().__init__(
            lable="My Node",
            type="Output",
            max_width=300,
            category="MyCategory"
        )

        # Add id for input field
        self.number_id = dpg.generate_uuid()

    # Define the input fields or widgets or whatever you want
    def compose(self):
        dpg.add_input_int(label="Number", default_value=0, tag=self.number_id, width=100, callback=self.update)
```

Create the function that will be called from the other nodes.
```python
import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyNode(Node):
    # Rest of the code ....

    def execute(self, data: NodePackage) -> NodePackage:
        # Get the data from the input field
        number = dpg.get_value(self.number_id)

        # Create a new package
        data.number = number
        data.string = "Hello World"

        return data
```

Make the save and load functions for the node.
```python
import dearpygui.dearpygui as dpg

from NodeEditor.Core.Node import Node
from NodeEditor.Core.NodePackage import NodePackage

class MyNode(Node):
    # Rest of the code ....

    # This function will be called when the node is saved to a file
    def on_save(self) -> dict:
        return {
            "number": dpg.get_value(self.number_id)
        }

    # This function will be called when the node is loaded from a file
    def on_load(self, data: dict):
        dpg.set_value(self.number_id, data["number"])
```

Now you have just made a basic output node.

## Different types of nodes
There are 6 different types of nodes that you can create. The types are:
### Input
This type of node only has a single input field. This type of node is mostly used in the end of the node chain or to visualize the data.

### Output
This type of node only has a single output field. This type of node is mostly used in the start of the node chain or to get the data.

### Both
This type of node has both an input and an output field. This type of node is mostly used to process the data.

### BothDualOut
This type of node has two output fields. This type of node is mostly used to process the data and output two different data.

### BothDualIn
This type of node has two input fields. This type of node is mostly used to get two different data and process it.

### DualInDualOut
This type of node has two input fields and two output fields. This type of node is mostly used to get two different data and output two different data.

## Node Configuration
<!-- lable: str,
        type: Literal["Input", "Both", "Output", "BothDualOut", "BothDualIn", "DualInDualOut"] = "Both",
        catagory: Literal["Inputs", "Output", "Filter"] | str = "All",
        max_width: int = 100,
        *,
        input_lable: str = "",
        input_lable_2: str = "",
        output_lable: str = "",
        output_lable_2: str = "",
    ) -> None: -->

The `Node` class has a few parameters that you can use to configure the node. The parameters are:
- `lable`: The name of the node that will be displayed on the node.
- `type`: The type of the node. The type of the node can be one of the following:
    - `Input`: This type of node only has a single input field.
    - `Output`: This type of node only has a single output field.
    - `Both`: This type of node has both an input and an output field.
    - `BothDualOut`: This type of node has two output fields.
    - `BothDualIn`: This type of node has two input fields.
    - `DualInDualOut`: This type of node has two input fields and two output fields.
- `catagory`: The category of the node. This is used in the menu to categorize the nodes. (Both on right click and the top menu)
- `max_width`: The maximum width of the node. This is used to make the node smaller or bigger.

The `Node` class also has some optional parameters that you can use to configure the node. The optional parameters are:
- `input_lable`: The name of the input field.
- `input_lable_2`: The name of the second input field.
- `output_lable`: The name of the output field.
- `output_lable_2`: The name of the second output field.

## Node Package
The `NodePackage` class is a class that is used to store the data that is passed between the nodes. The `NodePackage` class is a simple class that has some variables that can be used to store the data. The `NodePackage` class also has some functions that can be used to process the data.

## Advanced Node use
There are some advanced features that you can use to make the node system more powerful. The advanced features are:
- 'self.update': This function is can be called any time to update the state of a node. This might be used when changes in inputs are made, like a button click or a slider change. Just pass the 'self.update' function to the 'callback' parameter of the input field. Or you can call the 'self.update' function directly.
- 'self.on_error': This function can be called to show an error message on the node. This might be used when the data is not valid or the data is not in the correct format. It dose take a string as a parameter that will be displayed as an error message.
- 'def on_init(self) -> None': This function is called when the node is created. This might be used to set the default values of the input fields or to do some initial setup or if some data need to be cashed.

## About
This project was made by me (dron3fly3r) as a simple fun holiday project. The project is fully open source and can be used by anyone. The project is licensed under the MIT license. I will not be maintaining this project as it was just a fun project. If you want to contribute to the project, feel free to add new features, fix bugs or make the project better. If you have any questions or need help, feel free to contact me. So have fun and enjoy the project. 😄