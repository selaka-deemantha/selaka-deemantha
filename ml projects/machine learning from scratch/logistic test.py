import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from logistic_regression import LogisticRegression

bc=datasets.load_breast_cancer()
X,y=bc.data,bc.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=1234)

def accuracy(y_true,y_pred):
    accuracy=np.sum(y_true==y_pred)/len(y_true)
    return accuracy

re=LogisticRegression(lr=0.0001,n_iters=1000)
re.fit(X_train,y_train)
prediction=re.predict(X_test)

print('accuracy: ' , accuracy(y_test,prediction))
for i in range(len(prediction)):
    print(y_test[i] , prediction[i])