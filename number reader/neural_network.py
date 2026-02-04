import os
import matplotlib.pyplot as plt
from mnist_loader import load_mnist
import numpy as np
import random
import time

start_mega = time.time()
# --------------------------------------------------
# Resolve paths relative to THIS file (robust)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MNIST_DIR = os.path.join(BASE_DIR, "mnist")

# --------------------------------------------------
# Load MNIST (already parsed + normalized)
# --------------------------------------------------
X_train, y_train, X_test, y_test = load_mnist()


p = [16] # each element = no of neurons in that index layer
k = len(p) # = no of hidden layers
last_layer = X_train[0] # 0th layer = input layer
W = [] # = list for all the arrays of the weights
B = [] # = list for all the biases
Z = []

def ReLU(z):
    return np.maximum(0,z)
def softmax(z):
    z = z - np.max(z)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)
def sigmoid(z):
    return 1/(1+np.exp(-z))



for l in range(k):
    # calcuation for value for neurons + activation
    weights = np.random.randn(p[l], len(last_layer)) * np.sqrt(2 / len(last_layer))
    bias = np.zeros(p[l])
    value = ReLU(weights @ last_layer + bias)
    # updation in master sheet
    W.append(weights)
    B.append(bias)
    Z.append(value)
    # feeding to the next layer
    last_layer = value

# output layer

numbers = 10

w_out = np.random.randn(numbers, len(last_layer)) * np.sqrt(2 / len(last_layer))
b_out = np.zeros(numbers)
z_out = w_out @ last_layer + b_out
z_final = softmax(z_out)
W.append(w_out)
B.append(b_out)
Z.append(z_final)
y_true=np.zeros(10)
y_true[y_train[0]]=1

# training
lr = 0.005
epochs = 50

for epoch in range(epochs):

    start = time.time()

    for example in range(len(y_train)):
        '''if y_train[example]==3:
            continue'''
        # FORWARD PASS

        Z = []
        last_layer = X_train[example]

        for l in range(k):

            value = ReLU(W[l] @ last_layer + B[l])
            Z.append(value)
            last_layer = value

        z_out = W[k] @ last_layer + B[k]
        z_final = softmax(z_out)
        Z.append(z_final)

        # true label
        y_true = np.zeros(10)
        y_true[y_train[example]] = 1

        # BACKWARD PASS

        DW = []
        DB = []

        error = z_final - y_true

        for l in range(len(W)-1, -1, -1):

            prev_activation = X_train[example] if l == 0 else Z[l-1]

            dW = np.outer(error, prev_activation)
            dB = error

            DW.append(dW)
            DB.append(dB)

            if l > 0:
                error = W[l].T @ error
                error = error * (Z[l-1] > 0)

        # UPDATE

        for i in range(len(W)):
            W[i] -= lr * DW[::-1][i]
            B[i] -= lr * DB[::-1][i]

        '''if example%1000==0:

            correct = 0

            for i in range(len(X_test)):

                # forward pass (NO backprop)

                last_layer = X_test[i]

                for l in range(k):
                    last_layer = ReLU(W[l] @ last_layer + B[l])

                z_out = W[k] @ last_layer + B[k]
                probs = softmax(z_out)

                pred = np.argmax(probs)

                if pred == y_test[i]:
                    correct += 1

            accuracy = correct / len(X_test)
            print(f"Epoch {epoch+1}, Example {example} accuracy: {accuracy*100:.2f}%")'''
    
    
    correct = 0

    for i in range(len(X_test)):

        # forward pass (NO backprop)

        last_layer = X_test[i]

        for l in range(k):
            last_layer = ReLU(W[l] @ last_layer + B[l])

        z_out = W[k] @ last_layer + B[k]
        probs = softmax(z_out)

        pred = np.argmax(probs)

        if pred == y_test[i]:
            correct += 1
    
    step = epochs // 100   # 1% of epochs
    if epoch % (step+1) == 0:
        lr *= 0.99

    accuracy = correct / len(X_test)
    end = time.time()
    print(f"Epoch {epoch+1} accuracy: {accuracy*100:.2f}%, time taken: {round(end-start,1)}s")

    # random testing

    '''
    data_point = random.randint(0,len(X_test)-1)

    last_layer = X_test[data_point]

    for l in range(k):
        last_layer = ReLU(W[l] @ last_layer + B[l])

    z_out = W[k] @ last_layer + B[k]
    probs = softmax(z_out)
    pred = np.argmax(probs)

    img = X_test[data_point].reshape(28, 28)
    plt.imshow(img, cmap="gray", vmin=0, vmax=1)
    plt.title(f"True: {y_test[data_point]}, Pred= {pred}")
    plt.axis("off")
    plt.show()
    '''
end_mega = time.time()
print(f"Total time taken: {round(end_mega - start_mega,1)}s")