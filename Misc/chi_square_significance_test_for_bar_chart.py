# This code performs a Chi-Square Goodness of Fit test to determine if the observed counts in a bar chart
# are significantly different from an expected uniform distribution across categories.
# The null hypothesis is that the observed counts are consistent with the expected distribution.
# The p-value indicates the probability of observing the data if the null hypothesis is true.
# If the p-value is less than the significance level (commonly 0.05), we reject the null hypothesis,    
# suggesting that the observed distribution is significantly different from the expected distribution.
# If the p-value is greater than or equal to the significance level, we fail to reject the null hypothesis,
# indicating that the observed distribution is not significantly different from the expected distribution.

import scipy.stats as stats

# Observed counts from your bar chart
observed = [25, 35, 40]

# Expected counts if all categories are equally likely
total = sum(observed)
expected = [total / 3] * 3

# Perform the Chi-Square Goodness of Fit test
chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")
# Interpretation of the result
alpha = 0.05  # significance level
if p_value < alpha:
    print("Reject the null hypothesis: The observed distribution is significantly different from the expected distribution.")        
else:
    print("Fail to reject the null hypothesis: The observed distribution is not significantly different from the expected distribution.")
