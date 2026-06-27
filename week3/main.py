class Network:
    def __init__(self, weights_layers, bias_layers):
        self.weights_layers = weights_layers
        self.bias_layers = bias_layers
    
    def forward(self, inputs):
        current = inputs
        for layer_idx in range(len(self.weights_layers)):
            next_layer = []
            for i in range(len(self.weights_layers[layer_idx][0])):
                val = 0
                for j in range(len(current)):
                    val += current[j] * self.weights_layers[layer_idx][j][i]
                val += self.bias_layers[layer_idx][i]
                next_layer.append(val)
            current = next_layer

        return current


weights_hidden = [
    [0.5,  0.6],
    [0.2, -0.6],
]

weights_output = [
    [0.8],
    [0.4],
]

bias_hidden = [0.3, 0.25]
bias_output = [-0.5]

nn = Network(
    weights_layers=[weights_hidden, weights_output],
    bias_layers=[bias_hidden, bias_output]
)

print("-------- Task 1 --------")
outputs = nn.forward([1.5, 0.5])
print(outputs)

outputs = nn.forward([0, 1])
print(outputs)


weights_hidden = [
    [0.5,  0.6],
    [1.5, -0.8],
]

weights_hidden_sec = [
    [0.6],
    [-0.8],
]

weights_output = [
    [0.5, -0.4]
]



bias_hidden = [0.3, 1.25]
bias_hidden_sec = [0.3]
bias_output = [0.2, 0.5]

nn = Network(
    weights_layers=[weights_hidden, weights_hidden_sec, weights_output],
    bias_layers=[bias_hidden, bias_hidden_sec, bias_output]
)

print("-------- Task 2 --------")
outputs = nn.forward([0.75, 1.25])
print(outputs)

outputs = nn.forward([-1, 0.5])
print(outputs)