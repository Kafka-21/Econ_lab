# SVM classifier - fitting the widest possible street (represented by the parallel dashed lines) - large margin classification 
# adding more training instance "off the street" will not affect the decision boundary at all
# it is fully determined( or "supported") by the instance located on the edge of the stree. These instance are called support vectors
# check of senstivity of features scale

# soft margin classification 

# load iris dataset, scales the features and then trains a linear SVM mode(using the LinearSVC class with C=1 and the hinge loss)

import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = datasets.load_iris()
X = iris["data"][:, (2, 3)] # petal length, petal widht
y = (iris["target"] == 2).astype(np.float64) # Iris virginica

svm_clf = Pipeline([
				   ("scaler", StandardScaler()),
				   ("linear_svc", LinearSVC(C = 1, loss = "hinge")),
				   ])
svm_clf.fit(X, y)
print(svm_clf.predict([[5.5, 1.7]]))

# unlike Logistics Regression Classifiers, SVM classifiers do not output probabilities for each class 

# using SVC linear Kernel or SGDClassifier(loss = hinge, alpha = 1/ (m*C))
# applies regular SGD to train linear SVM classifier - it does not converge as fast as the linear SVC class, but it can be useful
# to handle online classification tasks or huge datasets that do not fit in memory(out-of-core training)

# Non - Linear SVM classification 

from sklearn.datasets import make_moons 
from sklearn.preprocessing import PolynomialFeatures

X, y = make_moons(n_samples = 100, noise = 0.15)
print(X, y)
polynomial_svm_clf = Pipeline([
							  ("poly_features", PolynomialFeatures(degree = 3)),
							  ("scaler", StandardScaler()),
							  ("svm_clf", LinearSVC( C = 10, loss = "hinge"))
							  ])
polynomial_svm_clf.fit(X,y)

# polynomial Kernel - Kernel trick for complex classification, avoid combinatorial explosion of number of features 

from sklearn.svm import SVC
poly_kernel_svm_clf = Pipeline([
							   ("scaler", StandardScaler()),
							   ("svm_clf", SVC(kernel = "poly", degree = 3, coef0 = 1, C = 5)) # 3 degree polynomial kernel
							   ])
poly_kernel_svm_clf.fit(X,y)

# coef0 controls how much the model is influenced by high degree polynomials versus low-degree polynomials
# Gridserach to fine tune hyperparameters

# Similarity features /function
# Gausssian Radial Basis function with gamma = 0.3 using landmark - transform data for better classification through adding new features 

rbf_kernel_svm_clf = Pipeline([
							  ("scaler", StandardScaler()),
							  ("svm_clf", SVC(kernel = "rbf", gamma = 5, C = 0.001))
							  ])
rbf_kernel_svm_clf.fit(X,y)

# increasing gamma makes the bell-shaped curve narrower - hence each isntance's range of influence is smaller
# the decision boundary ends up being more irregular, wiggling around individual instances
# a small gama value makes the bell shaped curve wider : instances have a large range of influence and teh decision boundary ends up smoother
# gamma - regularization hyperparameter 

# String Kernels - used when classifying text documents or DNA sequences (string subsequence Kernel or kernels based on Levenshtein distance)
# 1st approach - LinearSVC then SVC(kernel = linear) - if training set is not large - then go for Gaussian RBF 






























































