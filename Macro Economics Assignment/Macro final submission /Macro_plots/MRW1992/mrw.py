# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col
import matplotlib.pyplot as plt


# %%
data = pd.read_csv("/Users/quasar/downloads/Macro_plots/MRW1992/data/mrw.csv", header=0)


# %%
#convenience stuff
data = data.drop(data.columns[11], axis = 1)
data = data.drop(data.columns[0], axis = 1)
data = data.set_index('country')

data


# %%

#creating desired variables
data['ln(n + g + 𝛿)'] = np.log(data['popgrowth']/100 + 0.05)
data['ln(I / GDP)'] = np.log(data['i_y']/100)
data['CONSTANT'] = 1
data['ln(I / GDP) - ln(n + g + 𝛿)'] = data['ln(I / GDP)'] - data['ln(n + g + 𝛿)']

data


# %%
data['ln(SCHOOL)'] = np.log(data['school'])
data['ln(SCHOOL) - ln(n + g + 𝛿)'] = data['ln(SCHOOL)'] - data['ln(n + g + 𝛿)']
data['ln(Y60)'] = np.log(data['rgdpw60'])
data['ly85'] = np.log(data['rgdpw85'])
data['linv'] = np.log(data['i_y'])

#subsetting data
data_reg = data.loc[data['n'] == 1, :] #no oil
data_d = data_reg[data_reg.i == 1] #pop in 1960 less than 1 mil
data_oecd = data_reg[data_reg.o == 1] #oecd

data


# %%
#no restrictions on coefficients here
reg1 = sm.OLS(endog = data_reg['ly85'],
              exog = data_reg[['CONSTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
             missing = 'drop').fit()

reg2 = sm.OLS(endog = data_d['ly85'],
             exog = data_d[['CONSTANTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
             missing = 'drop').fit()

reg3 = sm.OLS(endog = data_oecd['ly85'],
             exog = data_oecd[['CONSTANTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
             missing = 'drop').fit()


# %%
# restricted model 
#coeff(log(savings)) = -coeff(log(n+g+d))
regr1 = sm.OLS(endog = data_reg['ly85'],
             exog = data_reg[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()

regr2 = sm.OLS(endog = data_d['ly85'],
             exog = data_d[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()

regr3 = sm.OLS(endog = data_oecd['ly85'],
             exog = data_oecd[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()


# %%
info_dict = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied α': lambda x: f"{x.params[1]/(1 + x.params[1]):.2f}"}

results_unres = summary_col(results = [reg1, reg2, reg3],
                           float_format='%0.2f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dict,
                           regressor_order = ['CONSTANT',
                                             'ln(I / GDP)',
                                             'ln(n + g + 𝛿)'])


results_res = summary_col(results = [regr1, regr2, regr3],
                           float_format='%0.2f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dict,
                           regressor_order = ['CONSTANT',
                                             'ln(I / GDP)',
                                             'ln(I / GDP) - ln(n + g + 𝛿)'])


results_res.add_title('Restricted Regressions')
results_unres.add_title('Unrestricted Regressions')
print(results_unres)
print('')
print(results_res)


# %%
# Human capital model
#no restrictions on coefficients here
regh1 = sm.OLS(endog = data_reg['ly85'],
             exog = data_reg[['CONSTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
             missing = 'drop').fit()

regh2 = sm.OLS(endog = data_d['ly85'],
             exog = data_d[['CONSTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
             missing = 'drop').fit()

regh3 = sm.OLS(endog = data_oecd['ly85'],
             exog = data_oecd[['CONSTANT', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
             missing = 'drop').fit()


# %%
#coeff(log(savings)) = -coeff(log(n+g+d))
reghr1 = sm.OLS(endog = data_reg['ly85'],
             exog = data_reg[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()

reghr2 = sm.OLS(endog = data_d['ly85'],
             exog = data_d[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()

reghr3 = sm.OLS(endog = data_oecd['ly85'],
             exog = data_oecd[['CONSTANT', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
             missing = 'drop').fit()


# %%
info_dictu = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied α': lambda x: f"{x.params[1]/(1 + x.params[1] + x.params[3]):.2f}",
            'Implied β': lambda x: f"{x.params[3]/(1 + x.params[1] + x.params[3]):.2f}"}

info_dictr = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied α': lambda x: f"{x.params[1]/(1 + x.params[1] + x.params[2]):.2f}",
            'Implied β': lambda x: f"{x.params[2]/(1 + x.params[1] + x.params[2]):.2f}"}

results_unres = summary_col(results = [regh1, regh2, regh3],
                           float_format='%0.2f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictu,
                           regressor_order = ['CONSTANT',
                                             'ln(I / GDP)',
                                             'ln(n + g + 𝛿)',
                                             'ln(SCHOOL)'])


results_res = summary_col(results = [reghr1, reghr2, reghr3],
                           float_format='%0.2f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictr,
                           regressor_order = ['CONSTANT',
                                             'ln(I / GDP)',
                                             'ln(I / GDP) - ln(n + g + 𝛿)',
                                             'ln(SCHOOL) - ln(n + g + 𝛿)'])


results_res.add_title('Restricted Regressions')
results_unres.add_title('Unrestricted Regressions')
print(results_unres)
print('')
print(results_res)


# %%
regcon1 = sm.OLS(endog = (data_reg['ly85'] - data_reg['ln(Y60)']),
               exog = data_reg[['CONSTANT', 'ln(Y60)']],
               missing = 'drop').fit()

regcon2 = sm.OLS(endog = (data_d['ly85'] - data_d['ln(Y60)']),
               exog = data_d[['CONSTANT', 'ln(Y60)']],
               missing = 'drop').fit()

regcon3 = sm.OLS(endog = (data_oecd['ly85'] - data_oecd['ln(Y60)']),
               exog = data_oecd[['CONSTANT', 'ln(Y60)']],
               missing = 'drop').fit()


# %%
info_dictroc = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied λ': lambda x: f"{-np.log(x.params[1] + 1)/25:.5f}"}

table_roc = summary_col(results = [regcon1, regcon2, regcon3],
                           float_format='%0.5f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictroc,
                           regressor_order = ['CONSTANT',
                                             'ln(Y60)'])

table_roc.add_title('Tests for Unconditional Convergence')
print(table_roc)


# %%
regcon4 = sm.OLS(endog = (data_reg['ly85'] - data_reg['ln(Y60)']),
               exog = data_reg[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
               missing = 'drop').fit()

regcon5 = sm.OLS(endog = (data_d['ly85'] - data_d['ln(Y60)']),
               exog = data_d[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
               missing = 'drop').fit()

regcon6 = sm.OLS(endog = (data_oecd['ly85'] - data_oecd['ln(Y60)']),
               exog = data_oecd[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)']],
               missing = 'drop').fit()



regcon7 = sm.OLS(endog = (data_reg['ly85'] - data_reg['ln(Y60)']),
               exog = data_reg[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
               missing = 'drop').fit()

regcon8 = sm.OLS(endog = (data_d['ly85'] - data_d['ln(Y60)']),
               exog = data_d[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
               missing = 'drop').fit()

regcon9 = sm.OLS(endog = (data_oecd['ly85'] - data_oecd['ln(Y60)']),
               exog = data_oecd[['CONSTANT', 'ln(Y60)', 'ln(I / GDP)', 'ln(n + g + 𝛿)', 'ln(SCHOOL)']],
               missing = 'drop').fit()


# %%
info_dictroc2 = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied λ': lambda x: f"{-np.log(x.params[1] + 1)/25:.5f}"}

table_roc2 = summary_col(results = [regcon4, regcon5, regcon6],
                           float_format='%0.5f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictroc,
                           regressor_order = ['CONSTANT',
                                             'ln(Y60)',
                                             'ln(I / GDP)',
                                             'ln(n + g + 𝛿)'])


table_roc3 = summary_col(results = [regcon7, regcon8, regcon9],
                           float_format='%0.5f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictroc,
                           regressor_order = ['CONSTANT',
                                             'ln(Y60)',
                                             'ln(I / GDP)',
                                             'ln(n + g + 𝛿)',
                                             'ln(SCHOOL)'])

table_roc2.add_title('Tests for Conditional Convergence')
table_roc3.add_title('Tests for Conditional Convergence')
print(table_roc2)
print(" ")
print(table_roc3)


# %%
regconr1 = sm.OLS(endog = (data_reg['ly85'] - data_reg['ln(Y60)']),
               exog = data_reg[['CONSTANT', 'ln(Y60)', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
               missing = 'drop').fit()

regconr2 = sm.OLS(endog = (data_d['ly85'] - data_d['ln(Y60)']),
               exog = data_d[['CONSTANT', 'ln(Y60)', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
               missing = 'drop').fit()

regconr3 = sm.OLS(endog = (data_oecd['ly85'] - data_oecd['ln(Y60)']),
               exog = data_oecd[['CONSTANT', 'ln(Y60)', 'ln(I / GDP) - ln(n + g + 𝛿)', 'ln(SCHOOL) - ln(n + g + 𝛿)']],
               missing = 'drop').fit()


# %%
info_dictrocr = {'R^2': lambda x: x.rsquared_adj,
            'Observations': lambda x: x.nobs,
            's.e.e.': lambda x: np.sqrt(x.scale),
            'Implied λ': lambda x: f"{-np.log(x.params[1] + 1)/25:.5f}"}
table_rocr = summary_col(results = [regconr1, regconr2, regconr3],
                           float_format='%0.5f',
                           stars = True,
                           model_names = ['Non-Oil',
                                         'Intermediate',
                                         'OECD'],
                           info_dict = info_dictroc,
                           regressor_order = ['CONSTANT',
                                             'ln(Y60)',
                                             'ln(I / GDP) - ln(n + g + 𝛿)', 
                                              'ln(SCHOOL) - ln(n + g + 𝛿)'])

table_rocr.add_title('Rate of Convergence - Restricted')
print(table_rocr)


# %%
reg_plt2 = sm.OLS(data_d['ln(Y60)'],
                 data_d[['ln(n + g + 𝛿)', 'linv']],
                 missing = 'drop').fit()
residln(Y60)1 = reg_plt2.resid

reg_plt3 = sm.OLS(data_d['ly85'] - data_d['ln(Y60)'],
                 data_d[['ln(n + g + 𝛿)', 'linv']],
                 missing = 'drop').fit()
residgr1 = reg_plt3.resid




reg_plt4 = sm.OLS(data_d['ln(Y60)'],
                 data_d[['ln(n + g + 𝛿)', 'linv', 'ln(SCHOOL)']],
                 missing = 'drop').fit()
residln(Y60)2 = reg_plt4.resid

reg_plt5 = sm.OLS(data_d['ly85'] - data_d['ln(Y60)'],
                 data_d[['ln(n + g + 𝛿)', 'linv', 'ln(SCHOOL)']],
                 missing = 'drop').fit()
residgr2 = reg_plt5.resid


# %%
fig, ax = plt.subplots(3, 1, sharex = 'col', figsize = (10, 12))
ax[0].scatter(data_d['ln(Y60)'], (data_d['ly85'] - data_d['ln(Y60)'])*100/25)
ax[0].set_xlabel('Log GDP Per Worker in 1960')
ax[0].set_ylabel('Growth Rate: 1960 - 1985')
ax[0].set_title('Unconditional')


ax[1].scatter(residln(Y60)1 + np.mean(data_d['ln(Y60)']), 
           (residgr1 + np.mean(data_d['ly85'] - data_d['ln(Y60)']))*100/25)
ax[1].set_xlabel('Log GDP Per Worker in 1960')
ax[1].set_ylabel('Growth Rate: 1960 - 1985')
ax[1].set_title('Conditional on saving and population growth')


ax[2].scatter(residln(Y60)2 + np.mean(data_d['ln(Y60)']), 
           (residgr2 + np.mean(data_d['ly85'] - data_d['ln(Y60)']))*100/25)
ax[2].set_xlabel('Log GDP Per Worker in 1960')
ax[2].set_ylabel('Growth Rate: 1960 - 1985')
ax[2].set_title('Conditional on human capital, saving and population growth')
plt.show()


# %%



