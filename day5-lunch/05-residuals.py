#!/usr/bin/env python3

"""
Usage: ./combine.py  <sample1/t_data.ctab> <sample2/t_data.ctab> etc
"""

import sys
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

compiled_means = {}

hist1 = sys.argv[1].split(os.sep)[-1]
mean1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0).iloc[:,4]
hist2 = sys.argv[2].split(os.sep)[-1]
mean2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = 0).iloc[:,4]
hist3 = sys.argv[3].split(os.sep)[-1]
mean3 = pd.read_csv(sys.argv[3], sep = "\t", index_col = 0).iloc[:,4]
hist4 = sys.argv[4].split(os.sep)[-1]
mean4 = pd.read_csv(sys.argv[4], sep = "\t", index_col = 0).iloc[:,4]
hist5 = sys.argv[5].split(os.sep)[-1]
mean5 = pd.read_csv(sys.argv[5], sep = "\t", index_col = 0).iloc[:,4]
#connect histone name to the mean value
fpkms_name = sys.argv[6].split(os.sep)[-1]
fpkm = pd.read_csv(sys.argv[6], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
compiled_means = {hist1 : mean1, hist2 : mean2, hist3 : mean3, hist4 : mean4, hist5 : mean5, fpkms_name : fpkm}

compiled_means_df = pd.DataFrame(compiled_means)

#fpkms_df.loc[roi_fpkm, :].to_csv(sys.stdout, sep = "\t", index = True)

#print(compiled_means_df)

compiled_means_df = compiled_means_df.dropna()


# y = np.dot(X, beta) + e
y = compiled_means_df.loc[:,fpkms_name]
X = compiled_means_df.loc[:,[hist1,hist2,hist3,hist4,hist5,]]
X = sm.add_constant(X)

model = sm.OLS(y, X)
# model = sm.OLS(y, X)
# print(model)
results = model.fit()
#print(results.summary())
# allresults = sm.regression.linear_model.RegressionResults(model, params = 6)
# print(allresults)


# def groupreg(g):
#     g['residual'] = sm.ols(formula=model, data=g).fit().resid
#     return g
#
# df = df.groupby('gp').apply(groupreg)
# print(df)
#compiled_means_df['yhat'] = results.fittedvalues
#compiled_means_df['resid'] = results.resid
#yhat = results.fittedvalues
resid = results.resid
# result2 = sm.OLS(df['y'], sm.add_constant(df[['x1', 'x2']])).fit()
# df['yhat2'] = result2.fittedvalues
# df['resid2'] = result2.resid

# predict doesn't return pandas series and no index is available
#compiled_means_df['predicted'] = results.predict(compiled_means_df)



# Y_pred = results.predict(y)
# #Y_pred = results.predict(y)
# residual = df[X].values-Y_pred
# print(Y_pred)
# print(residual)
# model_fitted_y = model_fit.fittedvalues
#
# # model residuals
# model_residuals = model_fit.resid
#
# # normalized residuals
# model_norm_residuals = model_fit.get_influence().resid_studentized_internal
#
# # absolute squared normalized residuals
# model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
#
# # absolute residuals
# model_abs_resid = np.abs(model_residuals)

fig, ax = plt.subplots()
ax.set_title("Histogram of Residuals")
plt.hist(resid)
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
# fig.savefig("residuals.png")
# plt.close()
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly( fig )
py.iplot(plotly_fig, filename='mpl-basic-histogram')
