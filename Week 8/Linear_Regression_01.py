# Linear Regression
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print(reg.coef_)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes datasets
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y = True)

#use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# split the data into training/testing Sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficient
print('coefficient: \n', regr.coef_)
# The mean squared Error
print("Mean squared error : %.2f"%mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f"%r2_score(diabetes_y_test, diabetes_y_pred))

# plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.plot(diabetes_X_test, diabetes_y_pred, color ='blue', linewidth = 3)

plt.xticks(())
plt.yticks(())

plt.show()
