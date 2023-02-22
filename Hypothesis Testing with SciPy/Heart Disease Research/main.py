import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test
# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
print(np.mean(chol_hd))
ttest, pvalue = ttest_1samp(chol_hd, 240)
print(pvalue/2)

chol_nhd= no_hd.chol
print(np.mean(chol_nhd))
ttest2, pvalue2 = ttest_1samp(chol_nhd, 240)
print(pvalue/2)

num_patients = len(heart)
print(num_patients)
num_highfbs_patients = len(heart[heart.fbs == 1])
print(num_highfbs_patients)
print(0.08*num_patients)

pvalue3 = binom_test(num_highfbs_patients, n=num_patients, p=0.08, alternative = "greater")
print(pvalue3)