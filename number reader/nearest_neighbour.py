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


# idx = 0   # change this to see different images

'''plt.imshow(train_img, cmap="gray")
plt.title(f"Label: {y_train[idx]}")
plt.axis("off")
plt.show()'''

X_train, y_train, X_test, y_test = load_mnist()
correct = 0
for img in range(100):
    test_img = X_test[img].reshape(28, 28)
    minimum = float('inf')
    minima = 0
    for idx in range(len(X_train)):
        train_img = X_train[idx].reshape(28, 28)
        final=(test_img.astype(float)-train_img.astype(float)).flatten()
        dist = np.sum(np.abs(final))
        if dist < minimum:
            #print(minimum, minima)
            minima = idx
            minimum = dist
    if y_test[img] == y_train[minima]:
        correct+=1
    #print(f"Accuracy: {round((correct*100)/(img+1))}%")
print(f"Accuracy: {round((correct*100)/100)}%")