import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

vein_pack_lifespans = familiar.lifespans(package="vein")
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
if vein_pack_test[1] < .05:
  print("The Vein Pack is Proven to Make You Live Longer!")
else:
  print("The Vein Pack is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package="artery")
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
if package_comparison_results[1] < .05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

iron_contingency_table = familiar.iron_counts_for_package()
chi2, pval, dof, expected = chi2_contingency(iron_contingency_table)
if pval < .05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We can't say the Artery Package will help you, i bet it's nice!")