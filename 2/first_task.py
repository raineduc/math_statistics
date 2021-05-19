import numpy as np
from math import sqrt

sample = np.array([0.3, 0.28, 0.27, 0.33, 0.35, 0.33, 0.27, 0.31, 0.37, 0.29])
n = len(sample)
confidence_level = 0.95
student_quantile = 2.262

sample_mean = sum(sample) / n
sample_variance = sum(sample ** 2) / (n - 1)  # corrected variance
standard_deviation = sqrt(sample_variance)


confidence_interval = [
    sample_mean - student_quantile * standard_deviation / sqrt(n),
    sample_mean + student_quantile * standard_deviation / sqrt(n)
]
