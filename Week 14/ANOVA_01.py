# delivery time for pizzas from 3 different companies

import pandas as pd

A = [12.6, 12, 11.8, 11.9, 13, 12.5, 14]
B = [10, 10.2, 10, 12, 14, 13]
C = [10.1, 13, 13.4, 12.9, 8.9, 10.7, 13.6, 12]

all_scores = A + B + C 
company_names = (['A'] * len(A)) + (['B'] * len(B)) + (['C'] * len(C))

data = pd.DataFrame({'company': company_names, 'score': all_scores})
# print(data,"\n")

# average delivery times per company give a first insight in which company is faster 
# print(data.groupby('company').mean(),"\n")

# average alone are not a good enough description of the situation as high variance in delivery of B
# to know need to do hypothesis test - within group variation and between group variation

import statsmodels.api as sm
from statsmodels.formula.api import ols

lm = ols('score ~ company', data= data).fit()
table = sm.stats.anova_lm(lm)
print(table)

# ANOVA using maths and python

# compute overall mean 
overall_mean = data['score'].mean()
# print("\noverall_mean : ",overall_mean)

# compute sum of squares total
data['overall_mean'] = overall_mean
ss_total = sum((data['score'] - data['overall_mean'])**2)
# print(ss_total)

# compute group means
group_means = data.groupby('company').mean()
group_means = group_means.rename(columns = {'score' : 'group_mean'})
# print(group_means)

# add group means and overall mean to the original data frame
data = data.merge(group_means, left_on='company', right_index = True)
# print(data)

# compute sum of squares residual
ss_residual = sum((data['score'] - data['group_mean'])**2)
print("\nss_residuals : ",ss_residual)

# Sum of squares total = sum of squares explained + sum of squares residual
# ss_explained = ss_total - ss_residuals 

# compute sum of squares model
ss_explained = sum((data['overall_mean_x'] - data['group_mean'])**2)
print("ss_explained : ", ss_explained)

# degree of freedom 
# df1 = df of the explained part = number of groups - 1 = 3 - 1 = 2
# df2 = df of the residual = number of observation - number of groups = 21 - 3 = 18

# statistical test of ANOVA is F-test 
# null hypothesis mean of all groups is equal - our model has no explanatory value i.e no proof for choosing one pizza company over another 
# alternative hypothesis states that at least one of the means is different which would be a reason to go more in-dept and find out which company or companies are faster

# compute mean_square_explained and mean_square_residual 

n_groups = len(set(data['company']))
n_obs = data.shape[0]
df_residual = n_obs - n_groups
ms_residual = ss_residual / df_residual
print("mean_square_residual : ", ms_residual)

df_explanied = n_groups - 1
ms_explained = ss_explained / df_explanied
print("mean_square_explained : ", ms_explained)

# F-statistics - use mean squares to compute the F statistics as ratio between explained vs unexplained variation 
# F = Mean_squared_explained / Mean_squared_residual

# compute F-Value
f = ms_explained / ms_residual
print("F-value : ", f)

# P-value - to decide whether an alternative hypothesis can be accepted or not
# if P-value is below 0.05 we reject the null hypothesis in favour of the alternative: this means that at least one group mean is significantly different 
# compute P-value using the F-distribution using df1 & df2 F(2,18)

import scipy.stats
p_value = 1- scipy.stats.f.cdf(f, df_explanied, df_residual)
print("P value : ",p_value)

"""
Our p-value of 0.45 is larger than 0.05, so we cannot reject our null hypothesis and 
we cannot accept our alternative. Even though the three sample means are different, we 
do not have a statistically significant difference. This means that with the observed data, 
there is not enough evidence to assume a general difference in delivery times of the three 
pizza companies

In our data, one pizza company was faster on average, but thanks to ANOVA we realize that 
this difference is not significant: we don’t have enough proof to conclude that one company 
is faster in general.

This perfectly illustrates the goal of statistical inference: telling whether an observed 
difference is significant or not.
"""

