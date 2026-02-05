import os
import matplotlib.pyplot as plt
from mnist_loader import load_mnist
import numpy as np
import random
import time

start_mega = time.time()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MNIST_DIR = os.path.join(BASE_DIR, "..", "datasets", "mnist")
MNIST_DIR = os.path.abspath(MNIST_DIR)

# --------------------------------------------------
# Load MNIST (already parsed + normalized)
# --------------------------------------------------


# idx = 0   # change this to see different images

'''plt.imshow(train_img, cmap="gray")
plt.title(f"Label: {y_train[idx]}")
plt.axis("off")
plt.show()'''

X_train, y_train, X_test, y_test = load_mnist()
correct1 = 0
correct2 = 0
dataset = 100

for img in range(dataset):
    test_img = X_test[img].reshape(28, 28)
    minimum1 = float('inf')
    minima1 = 0
    minimum2 = float('inf')
    minima2 = 0
    for idx in range(len(X_train)):
        train_img = X_train[idx].reshape(28, 28)
        final=(test_img.astype(float)-train_img.astype(float)).flatten()
        dist1 = np.sum(np.abs(final)) # mahattan distance
        dist2 = (np.sum(final**2))**(1/2) # Euclidean Distance
        if dist1 < minimum1:
            #print(minimum, minima)
            minima1 = idx
            minimum1 = dist1
        if dist2 < minimum2:
            #print(minimum, minima)
            minima2 = idx
            minimum2 = dist2
        
    if y_test[img] == y_train[minima1]:
        correct1+=1
    if y_test[img] == y_train[minima2]:
        correct2+=1
    print(f"Manhattan Accuracy: {round((correct1*100)/(img+1))}%")
    print(f"Euclidean Accuracy: {round((correct2*100)/(img+1))}%")
print(f"Manhattan Accuracy: {round((correct1*100)/dataset)}%")
print(f"Euclidean Accuracy: {round((correct2*100)/dataset)}%")