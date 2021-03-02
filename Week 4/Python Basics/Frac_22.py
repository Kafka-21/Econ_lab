# Wine quality testing using random forest 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

wine = pd.read_csv("/Users/quasar/Downloads/Python/winequality-red.csv")

print(wine.head())
quality_dist = wine['quality'].value_counts()
# plt.bar(quality_dist.index, quality_dist)
# plt.xlabel('quality')
# plt.ylabel('frequency')
# plt.show()

print(wine['quality'].describe())
