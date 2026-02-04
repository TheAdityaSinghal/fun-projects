import numpy as np
import struct
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MNIST_DIR = os.path.join(BASE_DIR, "mnist")

def load_images(path):
    with open(path, "rb") as f:
        magic, n, rows, cols = struct.unpack(">IIII", f.read(16))
        images = np.frombuffer(f.read(), dtype=np.uint8)
        images = images.reshape(n, rows * cols)
    return images

def load_labels(path):
    with open(path, "rb") as f:
        magic, n = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels

def load_mnist():
    X_train = load_images(os.path.join(MNIST_DIR, "train-images-idx3-ubyte"))
    y_train = load_labels(os.path.join(MNIST_DIR, "train-labels-idx1-ubyte"))
    X_test  = load_images(os.path.join(MNIST_DIR, "t10k-images-idx3-ubyte"))
    y_test  = load_labels(os.path.join(MNIST_DIR, "t10k-labels-idx1-ubyte"))

    X_train = X_train / 255.0
    X_test  = X_test / 255.0

    return X_train, y_train, X_test, y_test