import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_std = np.std(rottweiler_tl)
print(rottweiler_tl_mean, rottweiler_tl_std)

whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print(pval)

fstat, pval = f_oneway(fetchmaker.get_weight("whippet"), fetchmaker.get_weight("terrier"), fetchmaker.get_weight("pitbull"))
print(pval)

dogs = np.concatenate([fetchmaker.get_weight("whippet"), fetchmaker.get_weight("terrier"), fetchmaker.get_weight("pitbull")])
labels = ["whippet"] * len(fetchmaker.get_weight("whippet")) + ["terrier"]*len(fetchmaker.get_weight("terrier")) + ["pitbull"]*len(fetchmaker.get_weight("pitbull"))
tukey_results = pairwise_tukeyhsd(dogs, labels, 0.05)
print(tukey_results)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

# 	Poodle	Shih Tzu
# Black	x	x
# Brown	x	x
# Gold	x	x
# Grey	x	x
# White	x	x

poodle_black = np.count_nonzero(poodle_colors == "black")
poodle_brown = np.count_nonzero(poodle_colors == "brown")
poodle_gold = np.count_nonzero(poodle_colors == "gold")
poodle_grey = np.count_nonzero(poodle_colors == "grey")
poodle_white = np.count_nonzero(poodle_colors == "white")

shihtzu_black = np.count_nonzero(shihtzu_colors == "black")
shihtzu_brown = np.count_nonzero(shihtzu_colors == "brown")
shihtzu_gold = np.count_nonzero(shihtzu_colors == "gold")
shihtzu_grey = np.count_nonzero(shihtzu_colors == "grey")
shihtzu_white = np.count_nonzero(shihtzu_colors == "white")

X = [[poodle_black, shihtzu_black], [poodle_brown, shihtzu_brown], [poodle_gold, shihtzu_gold], [poodle_grey, shihtzu_grey], [poodle_white, shihtzu_white]]

chi2, pval, dof, expected = chi2_contingency(X)
print(pval)
