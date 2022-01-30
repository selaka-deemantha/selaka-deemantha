import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets


X,y=datasets.make_regression(n_samples=10000,n_features=2,noise=20,random_state=4)
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=1234)
print(X_test[0])
print(y_test[0])
from linear_regression import LinearRegression

regressor=LinearRegression(lr=0.002,n_iters=6000)
regressor.fit(X_train,y_train)
predicted=regressor.predict(X_test)

#415.1777339175251 [array([60.46264276,  7.64746643])] [4.738316307802732]

y=(0.28045294*(55.79384669))  + (0.47091551*96.60004458) + (-0.0628048330909294)
print(y)
#60.90263705948256