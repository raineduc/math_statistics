from first_task import confidence_interval as interval1, sample_mean as sample_mean1
from second_task import confidence_interval as interval2, sample_mean as sample_mean2

print("Доверительный интервал для первой задачи:")
print("({:.3f}, {:.3f})".format(interval1[0], interval1[1]))
print("Полученное выборочное среднее для первой задачи:")
print("{:.3f}".format(sample_mean1))
print("Доверительный интервал для второй задачи:")
print("({:.3f}, {:.3f})".format(interval2[0], interval2[1]))
print("Полученное выборочное среднее для второй задачи:")
print("{:.3f}".format(sample_mean2))
