#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


#load data
forests = pd.read_csv('forests.csv')

#check multicollinearity with a heatmap
corr_grid = forests.corr()
sns.heatmap(corr_grid, xticklabels=corr_grid.columns, yticklabels=corr_grid.columns, vmin=-1, center=0, vmax=1, cmap='PuOr', annot=True)
plt.show()
#plot humidity vs temperature
sns.lmplot(x="temp", y="humid", hue="region", markers=['o', 'x'], fit_reg=False, data=forests)
plt.show()
#model predicting humidity
modelH = sm.OLS.from_formula("humid ~ temp + region", data=forests).fit()
print(modelH.params)

#equation
#humid = 142.57 -7.24*region -2.39*temp

#plot regression lines
sns.lmplot(x="temp", y="humid", hue="region", markers=['o', 'x'], fit_reg=False, data=forests)
plt.plot(forests.temp, modelH.params[0] + modelH.params[1] + modelH.params[2]*forests.temp, color = "orange")
plt.plot(forests.temp, modelH.params[0] + modelH.params[1]*0 + modelH.params[2]*forests.temp, color = "blue")
plt.show()

#plot FFMC vs temperature
sns.lmplot(x="temp", y="FFMC", hue="fire", markers=['o', 'x'], fit_reg=False, data=forests)
plt.show()
#model predicting FFMC with interaction
modelF = sm.OLS.from_formula('FFMC ~ temp + fire + temp:fire', data=forests).fit()
resultsF = modelF.params
print(resultsF)

#plot regression lines
sns.lmplot(x="temp", y="FFMC", hue="fire", markers=['o', 'x'], fit_reg=False, data=forests)
plt.plot(forests.temp, resultsF[0] + resultsF[1] + resultsF[2]*forests.temp +resultsF[3]*forests.temp, color = "orange")
plt.plot(forests.temp, resultsF[0] + resultsF[1]*0 + resultsF[2]*forests.temp +resultsF[3]*forests.temp*0, color = "blue")
plt.show()
plt.clf()
#plot FFMC vs humid
plt.scatter(forests.humid, forests.FFMC)
plt.show()
#polynomial model predicting FFMC
modelP = sm.OLS.from_formula('FFMC ~ humid + np.power(humid,2)', data=forests).fit()
resultsP = modelP.params
print(resultsP)
#regression equation
## FFMC = 77.6 + 0.75*humid -0.01*humid^2

#sample predicted values
print(77.6 + 0.75*60 -0.01*60**2)


#multiple variables to predict FFMC
multiple = sm.OLS.from_formula('FFMC ~ + humid + temp + wind + rain', data=forests).fit()
print(multiple.params)
#predict FWI from ISI and BUI
multiple2 = sm.OLS.from_formula('FWI ~ ISI + BUI', data=forests).fit()
print(multiple2.params)