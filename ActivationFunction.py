import numpy as np

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