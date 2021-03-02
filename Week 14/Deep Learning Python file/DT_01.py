# Decision tree
from sklearn import tree

X = [[0,0], [1,1]]
Y = [0,1]

# fitting the model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# predicting 
clf.predict([[2., 2.]])


clf.predict_proba([[2.,2.]])


# using iris dataset
from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y = True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)
tree.plot_tree(clf)

