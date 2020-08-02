def relu(X):
    return np.maximum(0,X)

def step_function(x):
    res = x.copy() #Creates a copy to avoid overwriting input
    res[x<0] = 0
    res[x>=0] = 1
    return res

def sigmoid_function(x):
    return 1 / (1 + np.exp(x))