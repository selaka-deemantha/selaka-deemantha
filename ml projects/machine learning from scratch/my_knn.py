import numpy as np

class KNN:
    def __init__(self,k=3):
        self.k=k
    def euclidean_dis(self,x1,x2):
        # x1,x2 should be a numpy arrays
        return np.sqrt(np.sum((x1 - x2) ** 2))
    def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train

    def predict(self,X):
        predicted_labels=[self.execute(i) for i in X]
        return predicted_labels
    def execute(self,x):
        distence=[self.euclidean_dis(x,i) for i in self.X_train]
        k_nearest_neibors=np.argsort(distence)[:self.k]
        k_nearest_labels=[self.y_train[i] for i in k_nearest_neibors]
        most_common=np.bincount(k_nearest_labels).argmax()
        return most_common
