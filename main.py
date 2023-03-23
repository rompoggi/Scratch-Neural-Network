import NNet as nn

def main():

    NN = nn.NNet()

    layer1 = nn.Layer()
    node1 = nn.Node(0.5)
    node2 = nn.Node(0.3)
    node3 = nn.Node(0.2)
    layer1.add_nodes([node1,node2,node3])
    layer1.set_id(1)

    layer2 = nn.Layer()
    node1 = nn.Node(0.9)
    node2 = nn.Node(0.5)
    node3 = nn.Node(0.3)
    node4 = nn.Node(0.12)
    node5 = nn.Node(0.1)
    node6 = nn.Node(12)
    layer2.add_nodes([node1,node2,node3,node4,node5,node6])
    layer2.set_id(2)

    NN.add_layer(layer1)
    NN.add_layer(layer2)

    Activation = nn.ActivationFunction()
    Activation.binary()
    NN.activation_function = Activation

    # neural_net.set_activation(lambda x: x)

    print(repr(NN))

if __name__ == '__main__':
    main()