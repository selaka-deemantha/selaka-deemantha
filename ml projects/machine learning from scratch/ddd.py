import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
X,y=iris.data,iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1234)


from my_knn import KNN
clf=KNN()
clf.fit(X_train,y_train)
predictions=clf.predict(X_test)


print(predictions)
print(y_test)
