import math
import matplotlib.pyplot as plt
import numpy as np

def spearman_rank_correlation(X, Y, N):
    d = 0
    for i in range(N):
        d += math.pow(X[i] - Y[i], 2)
    return 1 - (6 * d / (N * (math.pow(N, 2) - 1)))

def zip_rank(arr):
    index = range(0, len(arr))
    rank = range(1, len(arr)+1)
    arr = sorted(zip(sorted(zip(arr, index)), rank), key=lambda x: x[0][1])
    return list(map(lambda x: x[1], arr))

def mean(arr):
    return sum(arr) / len(arr)

def deviation(arr):
    arr_m = mean(arr)
    s = 0
    for x in arr:
        s += math.pow(x - arr_m, 2)
    return s / math.sqrt(len(arr)) 

if __name__ == "__main__":
    scores = [(95, 85), (85, 95), (80, 70), (70, 65), (60, 70)]

    N = len(scores)
    X = zip_rank(list(map(lambda x: x[0], scores)))
    Y = zip_rank(list(map(lambda x: x[1], scores)))
    s = spearman_rank_correlation(X, Y, N)

    b = s * deviation(Y) / deviation(X)
    a = mean(Y) - mean(X) * b

    print(a, b)
    X = list(map(lambda x: x[0], scores))
    Y = list(map(lambda x: x[1], scores))
    plt.scatter(X, Y, color='r')

    x_points = np.arange(60, 100, 1)
    y_points = b * x_points + a
    plt.plot(x_points, y_points)
    plt.show()
    
    y = b * 80 + a
    print(y)