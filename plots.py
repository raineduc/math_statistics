import matplotlib.pyplot as plt
import numpy as np


def draw_step_plot(x, func):
    x_arr = np.concatenate([x, [max(x) + 0.0001]])
    y = func(x_arr)
    plt.step(x_arr, y)
    plt.title('Эмпирическая функция распределения')
    plt.savefig('Функция распределения.png')
    plt.grid(color='0.8')
    plt.show()


def draw_hist(x):
    plt.hist(x, bins='sturges', edgecolor='black', density=True)
    plt.title('Гистограмма частостей')
    plt.savefig('Гистограмма частостей.png')
    plt.show()


def draw_polygon(x):
    hist, bins = np.histogram(x, bins='sturges', density=True)
    plt.plot(bins[:-1], hist)
    plt.grid(color='0.8')
    plt.title('Полигон частостей')
    plt.savefig('Полигон частостей.png')
    plt.show()
