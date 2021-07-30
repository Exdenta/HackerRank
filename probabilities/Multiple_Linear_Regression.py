# import numpy as np

# if __name__ == "__main__":
#     X1 = [5, 6, 7, 8, 9]
#     X2 = [7, 6, 4, 5, 6]
#     Y = [10, 20, 60, 40, 50]
#     N = len(Y)
#     X_count = 2

#     X = np.ones((N, X_count + 1))
#     X[:, 0] = np.ones(N)
#     X[:, 1] = X1
#     X[:, 2] = X2

#     result = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), Y)
#     print(result.shape)
#     x1 = 5
#     x2 = 5
#     b = [1, x1, x2]
#     result = np.dot(b, result)
#     print(result)



import numpy as np

if __name__ == "__main__":
    # m, n = tuple(map(int, input().strip().split()))
    # X = np.empty((m+1, n-1))
    # for i in range(n-1):
    #     X[:, i] = list(map(float, input().strip().split()))
    # Y = list(map(float, input().strip().split()))
    m, n = 2, 7
    X = np.ones((m + 1, n))
    X[:, 0] = np.ones(m + 1)
    X[:, 1] = np.array([0.18, 0.89, 109.85])
    X[:, 2] = np.array([1.0, 0.26, 155.72])
    X[:, 3] = np.array([0.92, 0.11, 137.66])
    X[:, 4] = np.array([0.07, 0.37, 76.17])
    X[:, 5] = np.array([0.85, 0.16, 139.75])
    X[:, 6] = np.array([0.99, 0.41, 162.6])
    Y = [0.87, 0.47, 151.77]

    #center
    X_R = X-np.mean(X,axis=0)
    Y_R = Y-np.mean(Y)
    #calculate beta
    beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))
    print(beta.shape)
    print(beta)


    B = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    
    inp = [(0.49, 0.18), (0.57, 0.83), (0.56, 0.64), (0.76, 0.18)]
    for x1, x2 in inp:
        # x1, x2 = tuple(map(float, input().strip().split()))
        x = [1, x1, x2]
        print(np.dot(x, B))




