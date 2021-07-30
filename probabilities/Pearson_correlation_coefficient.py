import math
import matplotlib.pyplot as plt
import numpy as np

""" Correlation and Regression Lines - A Quick Recap #1
"""

def mean(X):
    return sum(X) / len(X)

def standart_deviation(X):
    s = 0
    xm = mean(X)
    for x in X:
        s += math.pow(x - xm, 2)
    return math.sqrt(s / len(X))

def covariation(X, Y):
    s = 0
    xm = mean(X)
    ym = mean(Y)
    for x, y in zip(X, Y):
        s += (x - xm) * (y - ym)
    return s / len(X)

if __name__ == "__main__":
        physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
        history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

        physics = [95, 85, 80, 70, 60]
        history = [85, 95, 70, 65, 70]
        
        Pearson_Correlation_Coefficient = covariation(physics, history) / (standart_deviation(physics) * standart_deviation(history))
        print(Pearson_Correlation_Coefficient)
        # plt.scatter(physics, history)
        # plt.show() 