import col as c
import numpy as np

class Node():

    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return str(self.weight)
    
    def __repr__(self):
        return str(self.weight)
    

class Layer():

    def __init__(self):
        self.layer_index = 0
        self.nodes = []
        self.node_count = 0

    def set_id(self, ID):
        self.layer_index = ID


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

    def add_nodes(self, nodes):
        self.nodes.extend(nodes)
        self.node_count += len(nodes)

    def __str__(self) -> str:
        if self.node_count >= 5:
            out = f"Layer {self.layer_index}, {self.node_count} nodes: {self.nodes[0]}, {self.nodes[1]}, {self.nodes[2]}, ... , {self.nodes[self.node_count-1]}"
            return out
        
        out = f"Layer {self.layer_index}, {self.node_count} nodes:"
        for j in range(self.node_count):
            out += f" {self.nodes[j]}"

        return out
        # return f"Layer {self.layer_index}, {self.node_count} nodes: {self.nodes}"



    def __repr__(self) -> str:
        print(str(self))


class NNet():

    def __init__(self):
        self.layers = []
        self.layer_count = 0
        self.total_nodes = 0

        self.activation_function = ActivationFunction()



    ## Getting attributes

    def get_activation(self):
        return self.activation_function
    
    def set_activation(self, activation):
        self.activation_function = activation


    def add_layer(self, layer):
        self.layers.append(layer)
        self.layer_count += 1
        self.total_nodes += layer.node_count

    def insert_layer(self, index, layer):
        self.layers.insert(index, layer)
        self.layer_count += 1
        self.total_nodes += layer.node_count

    def get_layer(self, index):
        return self.layers[index]
    
    def get_layer_count(self):
        return self.layer_count
    
    def get_layers(self):
        return self.layers

    ## Debugging

    def __str__(self) -> str:

        col = c.col()
        out = ''

        out += col.header_('Neural Network :')
        out += col.okcyan_(f' Layer count : {self.layer_count}, Total nodes: {sum([x.node_count for x in self.layers])} \n')
        out += col.okblue_(f'Activation function: {col.warn_(str(self.activation_function))}\n')

        for layer in self.layers:
            out += col.ok_(f'{layer}\n')

        # for i, layer in enumerate(self.layers):
        #     out += col.ok_(f'{layer}\n')

        return out

    def __repr__(self) -> str:
        return str(self)


class ActivationFunction():

    def __init__(self):
        self.function = lambda x: x
        self.name = 'linear'
        self.string = 'x -> x'


    def binary(self):
        self.function = lambda x: 1 if x > 0 else 0
        self.name = 'binary'
        self.string = 'x -> 1 if x > 0 else 0'

    def sigmoid(self):
        self.function = lambda x: 1 / (1 + np.exp(-x))
        self.name ='sigmoid'
        self.string = 'x -> 1 / (1 + exp(-x))'

    def tanh(self):
        self.function = lambda x: np.tanh(x)
        self.name = 'tanh'
        self.string = 'x -> tanh(x)'

    def relu(self):
        self.function = lambda x: np.maximum(0, x)
        self.name ='relu'
        self.string = 'x -> max(0, x)'

    def softmax(self):
        self.function = lambda x: np.exp(x) / np.sum(np.exp(x), axis=0)
        self.name ='softmax'
        self.string = 'x -> exp(x) / sum(exp(x)'

    def parametric_relu(self,alpha=0.1):
        self.function = lambda x: np.maximum(alpha * x, x)
        self.name = 'leaky_relu'
        self.string = 'x -> max({alpha} * x , x)'

    def leaky_relu(self):
        self.parametric_relu(alpha=0.1)

    def linear(self):
        self.function = lambda x: x
        self.name = 'linear'
        self.string = 'x -> x'

    def ELU(self,alpha=1):
        self.function = lambda x: x if x >= 0 else alpha * (np.exp(x) - 1)
        self.name = 'ELU - Exponential Linear Unit'
        self.string = 'x -> x if x >= 0 else {alpha} * (exp(x) - 1)'

    def swish(self):
        self.function = lambda x: x / ( 1 + np.exp(-x))
        self.name ='swish'
        self.string = 'x -> x * sigmoid(x) = x * (1 + exp(-x))'

    def get_name(self):
        return self.name
    
    def get_string(self):
        return self.string
    
    def get_function(self):
        return self.function
    
    def __str__(self) -> str:
        return f'{self.name} : {self.string}'

    def __repr__(self) -> str:
        return self.string