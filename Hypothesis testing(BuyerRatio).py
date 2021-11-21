# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:16:09 2020

@author: Wellson
"""

import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm

Buyer=pd.read_csv("C:/Users/Wellson/Documents/R/360/Hypothesis testing/BuyerRatio.csv")
Buyer

help(stats.ttest_1samp)
print(stats.ttest_ind(Buyer.East))
help(stats.test)

scipy.stats.ttest_ind(Buyer.East,Buyer.West)
scipy.stats.ttest_ind(Buyer.North,Buyer.South)
