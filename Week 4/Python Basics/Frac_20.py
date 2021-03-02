# cross validation - to tackle problem of overfitting 

""" 
Cross validation techniques but the overall concept remains same
- to parition the data into a number of subsets
- hold out a set at a time and train the model on remaining set
- Test model on hold out set 

Types of cross Validation
- K- Fold Cross validation 
- Stratified K- Fold cross Validation 
- Leave one out cross validation 

K- Fold cross validation - dataset divided into 5 equal parts and the below process will run 5 times, each time 
with a different holdout set
- take the group as a holdout or test dataset
- take the remaining groups as traingin data set
- fit a model on the training set and evaluate it on test set
- retain the evaluation score and discard the model 


"""

from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score

diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]
lasso = linear_model.Lasso()
print(cross_val_score(lasso, X, y, cv=3))





