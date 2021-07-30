import math
import matplotlib.pyplot as plt
import numpy as np

def mean(X):
    return sum(X) / len(X)

def deviation(X):
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
    scores = [(95, 85), (85, 95), (80, 70), (70, 65), (60, 70)]

    N = len(scores)
    X = list(map(lambda x: x[0], scores))
    Y = list(map(lambda x: x[1], scores))
    pearson = covariation(X, Y) / (deviation(X) * deviation(Y))

    b = pearson * deviation(Y) / deviation(X)
    a = mean(Y) - mean(X) * b

    x_points = np.arange(60, 100, 1)
    y_points = b * x_points + a
    plt.plot(x_points, y_points)
    plt.scatter(X, Y, color='r')
    plt.show()
    
    y = b * 80 + a
    print(round(y, 3))