from statistics import mean, pstdev


def pearson(x, y):
    mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (len(x) * sx * sy)


def linear_regression(x, y):
    b = pearson(x, y) * pstdev(y) / pstdev(x)
    return mean(y) - b * mean(x), b


    scores = [(95, 85), (85, 95), (80, 70), (70, 65), (60, 70)]

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
p = pearson(x, y)
print(p)
a, b = linear_regression(x, y)
print(a, b)
print(f'{a+b*80:.3f}')
