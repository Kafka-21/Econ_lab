# Decision Tree

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier 

iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target 

tree_clf = DecisionTreeClassifier(max_depth = 2)
tree_clf.fit(X, y)

# visualization the trained decision tree 
"""
from sklearn.tree import export_graphviz

export_graphviz(
				tree_clf,
				out_file = "/Users/quasar/Downloads/Python/Machine_Learning_Handbook/iris_tree.dot",
				feature_names = iris.feature_names[2:],
				class_names = iris.target_names, 
				rounded = True, 
				filled = True 
				)

"""
# Decision Trees is that they require very little data preparation and do not require feature scaling or centering at all
# node gini attribute  measure its impurity - a node is pure (gini = 0) if all training instances it applies to belong to the same class

# Scikit learn uses the CART algorithm which produces only binary trees : non-leaf nodes always have 2 children(ie questions only have yes/No answers)
# however, other algorith,s such as ID3 can produce Decision tress with nodes that have more than two children

# White box model - Decision Tree while Black Box model - Random Forest and ANN

# estimating class probablities 

print(tree_clf.predict_proba([[5, 1.5]]))
print(tree_clf.predict([[5, 1.5]]))

# The CART(classification and Regression Tree) training Algorithm to train Decision Tree 
# CART splits training data using single feature k and a threshold tk
# chooses values of k and tk to produce the purest subsets
# cost function that the algorithm tries to minimize 
# once CART successfully split the training data set into two, it splits subsets using the same logic and then recursively continues
# IT stops recursing once it reaches the maximum depts( max_depth hyperparameter)
# other hyperparameters ( min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_leaf_nodes)
# CART aglorithm is greedy algorithm (hence only reasonable good solution not optimal)
# NP-Complete proble - finding the optimal tree

# Entropy - zero when it contains instances of only one class (gini impurity vs entropy debate)
# gini impurity tends to isolate the most frequent class in its own branch of the tree, while entropy tends to produce slightyl more balanced trees
# Regularization Hyperparameters - parametric model vs nonparametric model 
# Parametric model - linear model has a pre-determined number of parameters, so its degree of freedom is limited, reducing the risk of overfitting(but increasing the risk of underfitting )
# To avoid overfitting the training data, need to restrict the Decision Tree' freedom during training. -> This is called regularization
# The regularization hyperparameters depend on the algorithm used, but generally you can at least restrict the maximum depth of the decision Tree.
# Reducing max_depth will regularize the model and thus reduce the risk of overfitting

# other algorithm - 1st training the Decision Tree without restriction, then pruing (deleting) unnecessary nodes. 
# A node whose children are all leaf nodes is considered unnecessary if the purity improvement is not statistically significant
# Chi-squared test are used to estimate the probabilty that the improvement is purely the result of chance( which is called the null-hypothesis)
# If this probability - called p value is higher than a given threshold - the node is considered unnecessary and its children are deleted. 
# Pruning continues untill all unnecessary nodes have been pruned

# DecisionTreeRegressor training noisy quadratic dataset with max_depth = 2

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth = 2)
tree_reg.fit(X, y)

# Decision tree (instablity)- all splits are perpendicular to an axis - sensitive to training set rotation 
# orientation of datasets  can lead to convoluted decision tree - hence PCA
# Decision tree - sensitive to small variation in the training data. 
# outliner affect decision tree 
# training algorithm is stochastic = different model even on the same training data ( therefore set random_state  hyperparameter)







































































