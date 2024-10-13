import time
import copy

class NodePackage:
    number: int
    string: str
    
    def text(self) -> str:
        return f"{self.number} {self.string}"
    
    def copy(self) -> 'NodePackage':
        new_package = NodePackage()
        for key, value in self.__dict__.items():
            setattr(new_package, key, copy.deepcopy(value))
        return new_package