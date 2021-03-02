import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
print(list(iris.keys()))
# print(iris)

X = iris["data"][:, 3:] # petal width
# print(X)
y = (iris["target"] == 2).astype(np.int) # 1 if Iris virginica, else 0

from sklearn.linear_model import LogisticRegression 

log_reg = LogisticRegression()
log_reg.fit(X, y)

#model's estimated probabilities for flowers with petal widths varying from 0 to 3 cm 

X_new = np.linspace(0, 3, 1000).reshape(-1, 1) # linspace create 1000 numbers between 0 and 3 and reshape vectorized it 
# print(X_new)
y_proba = log_reg.predict_proba(X_new)
plt.plot(X_new, y_proba[:, 1], "g-", label = "Iris virginica")
plt.plot(X_new, y_proba[:, 0], "b--", label = "Not Iris virginica")
plt.show() # observe plot to check for probablities of classification and their confidence (through decision boundary)

print(log_reg.predict([[1.7], [1.5]]))

# Softmax regression for multilcass classification 

X = iris["data"][:, (2, 3)] # petal length, petal width
y = iris["target"]

softmax_reg = LogisticRegression(multi_class = "multinomial", solver = "lbfgs", C = 10)
softmax_reg.fit(X,y)

print(softmax_reg.predict([[5, 2]]))
print(softmax_reg.predict_proba([[5, 2]]))











