import numpy as np
from collections import Counter


def eucidean_distence(x1,x2):
    """"
    we can find distance of two coordinates  (any dimention) using this funtion
    """
    #x1,x2 should be a numpy arrays
    return np.sqrt(np.sum((x1-x2)**2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        print(111111)
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # compute distences
        distences = [eucidean_distence(x, x_train) for x_train in self.X_train]
        # get k nearest labels,samples
        k_indices = np.argsort(distences)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # most common class labels
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
