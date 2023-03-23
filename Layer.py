import numpy as np

class layer():

    def __init__(self):
        self.layer_number = 0
        self.nodes = []
        self.node_count = 0


    def weight_list(self):
        weight_list = []
        for node in self.nodes:
            weight_list.append(node.weight)
        return np.array(weight_list)
    
    def node_list(self):
        return self.nodes
    
    def add_node(self, node):
        self.nodes.append(node)
        self.node_count += 1

    def __str__(self) -> str:
        if self.node_count >= 5:
            return f"Layer {self.layer_number} has {self.node_count} nodes"
    
    def __repr__(self) -> str:
        print(str(self))
