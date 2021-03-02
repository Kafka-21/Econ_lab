#  SVM Regression tol used for regression  

from sklearn.svm import LinearSVR

iris = datasets.load_iris()
X = iris["data"][:, (2, 3)] # petal length, petal widht
y = (iris["target"] == 2).astype(np.float64) # Iris virginica

svm_reg = LinearSVR(epsilon = 1.5)
svm_reg.fit(X, y)

# using kernelizied SVM for nonlinear regression tasks
# large C - little regularization , small C - large regularization 

# kernel trick
from sklearns.svm import SVR

svm_poly_reg = SVR(kernel = "poly", degree = 2, C = 100, epsilon = 0.1 )
svm_poly_reg.fit(X, y)
