from math import sqrt
import numpy as np
from plots import draw_step_plot, draw_hist, draw_polygon

sample = np.array([0.92, 0.51, -1.05, -1.41, 1.04, -1.03, 1.55, -0.17, 0.92, 0.17,
                   0.41, 1.63, -1.53, -0.20, 0.85, 0.09, 1.54, 0.25, 1.24, -0.26])

variation_range = sorted(sample)
sample_max = max(sample)
sample_min = min(sample)
sample_span = sample_max - sample_min
sample_mean = sum(sample) / len(sample)
sample_variance = sum(sample ** 2) / len(sample)
standard_deviation = sqrt(sample_variance)

empirical_distribution = np.vectorize(lambda x: np.count_nonzero(sample < x) / len(sample))
draw_step_plot(variation_range, empirical_distribution)
draw_hist(variation_range)
draw_polygon(variation_range)


def join_num_array(num_arr):
    return '\n' + ' '.join(map(str, num_arr))


print('Выборка: {}'.format(join_num_array(sample)))
print('Вариационный ряд: {}'.format(join_num_array(variation_range)))
print('Максимум выборки: {}'.format(sample_max))
print('Минимум выборки: {}'.format(sample_min))
print('Выборочное среднее: {}'.format(sample_mean))
print('Среднеквадратичное отклонение: {}'.format(standard_deviation))
