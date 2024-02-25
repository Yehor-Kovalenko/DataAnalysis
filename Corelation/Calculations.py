import math


def average(charac):
    summary = 0.0
    i = 0
    while i < len(charac):
        summary += charac[i]
        i += 1
    return summary / len(charac)



def stand_deviation(charac):
    sum_sqr_deviation = 0
    i = 0
    while i < len(charac):
        sum_sqr_deviation += (charac[i] - average(charac)) ** 2
        i += 1
    return math.sqrt(sum_sqr_deviation / (len(charac) - 1))


def covariation(x, y):
    i = 0
    summary = 0
    while i < len(x):
        summary += ((x[i] - average(x)) * (y[i] - average(y)))
        i += 1
    return summary / (len(x) - 1)


def pearson(x, y):
    return covariation(x, y) / (stand_deviation(x) * stand_deviation(y))


def slope_a(x, y):
    summary = 0
    for i in range(len(x)):
        summary += ((x[i] - average(x)) * (y[i] - average(y)))

    sum_sqr_deviation = 0
    for i in range(len(x)):
        sum_sqr_deviation += (x[i] - average(x)) ** 2
    return summary / sum_sqr_deviation


def init_value_b(x, y):
    return average(y) - (slope_a(x, y) * average(x))


