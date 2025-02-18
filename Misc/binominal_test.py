from scipy.stats import binomtest

# Number of successes (e.g., heads)
successes = 15

# Number of trials (e.g., coin flips)
trials = 20

# Hypothesized probability of success
p0 = 0.5

# Perform the binomial test
p_value = binomtest(successes, trials, p0, alternative='two-sided')

print(f'P-value: {p_value}')
