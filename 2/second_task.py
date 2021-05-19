from math import sqrt

n = 64
confidence_level = 0.99
SX = 5424.8  # sum(x_k)
SXX = 973.44  # sum(x_k^2)
T_y = 2.575

sample_mean = SX / n
sample_variance = SXX / n
standard_deviation = sqrt(sample_variance)


confidence_interval = [
    sample_mean - T_y * standard_deviation / sqrt(n),
    sample_mean + T_y * standard_deviation / sqrt(n)
]

