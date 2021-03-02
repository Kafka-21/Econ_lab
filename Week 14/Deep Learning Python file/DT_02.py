# decision tress - supervised learning method - both regressison & classification , prone to overfitting 
# anatony of classification trees (depth of a tree, root nodes, decision nodes, leaf nodes, terminal nodes)
# Classification trees are greedy algorithm which means by default it will continue to split until it has a pure node
# deep classification can lead to overfitting of data
# scikit-learn allows to preprune decision trees - allows to set maximum depth to stop growth of tree
# selection criteria  - 'gini' or 'entropy'- information gain - good split point for root or decision nodes on classification trees
# decision tree split on feature and corresponding split point the results in largest information gain 
# IG = information before splitting (parent) - information after splitting (children)

# Code 
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
df = pd.DataFrame(data.data, columns= data.feature_names)
df['target'] = data.target
# print(df.head())

# splitting data into training and test sets 75-25 % partition
X_train, X_test, Y_train, Y_test = train_test_split(df[data.feature_names], df['target'], random_state=0)
print(X_train)

# advantage over PCA and logistic regression - not sensitive to effects of not standardizing your data
from sklearn.tree import DecisionTreeClassifier

# max_depth of tree = 2 
clf = DecisionTreeClassifier(max_depth = 2, random_state = 0)

# train the model on data  X(sepal length, sepal width, petal length, petal width) and Y(species)
clf.fit(X_train, Y_train)

# Predict labels of unseen data for 1 observation 
clf.predict(X_test.iloc[0].values.reshape(1,-1))

# Predict labels for multiple observation 
clf.predict(X_test[0:10])

# Measuring model performance - F1 score, ROC curve, precision recall 
# accuracy = correct predictions / total number of data points 

# score method returns the accuracy of the model 
score = clf.score(X_test, Y_test)
print("\nScore in depth  1  : ", score, "\n")

# Tuning the depth of tree

# List of values to try for max_depth 
max_depth_range = list(range(1,10))
# List to store the average RMSE for each value of max_depth:
accuracy = []

for depth in max_depth_range:
	clf = DecisionTreeClassifier(max_depth = depth, random_state =0)
	clf.fit(X_train, Y_train)
	score = clf.score(X_test, Y_test)
	accuracy.append(score)
	print("Score in depth ",depth," : ",score)

# depth of decision_tree need not equal to max_depth
# depth of decision_tree using get_depth method , get number of leaf nodes for a trained decision tree by using get_n_leaves
# other parameters to tune - min_samples_leaf and max_leaf_nodes 
""" classification trees in scikit learn allow you to calculate feature importance which is the total
amount that gini index or entropy decrease due to splits over a given feature. Scikit-learn outputs a number 
between 0 and 1 for each feature. All feature importances are normalized to sum to 1."""

# importance of decision tree model 
importances = pd.DataFrame({'feature' : X_train.columns,
	 						'importance' : np.round(clf.feature_importances_,3)})
importances = importances.sort_values('importance', ascending= False)

print("importances : \n", importances)

