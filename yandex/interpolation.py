
"""
Interpolation
https://contest.yandex.ru/contest/28413/problems/E/

Есть некоторый многочлен второй степени от 5 переменных f(x1, x2, x3, x4, x5), с помощью которого были получены
значения в некотором наборе точек. По этому набору точек и значениях в них надо предсказать значения в другом наборе
точек с абсолютной или относительной точностью 10-6.

Формат ввода
На вход подаётся файл из 1000 тренировочных точек вместе со значением и 1000 тестовых точек.
Более формально сразу идёт 1000 строк тренировочной выборки, состоящих из 6 действительных чисел,
разделённых табуляцией ('\t'). Первые 5 из этих 6 чисел – задают переменные x1...x5. Последнее число задаёт
значение функции в этой точке. Затем идёт 1000 строк тестовой выборки, состоящих из 5 действительных чисел,
разделённых табуляцией. Все они задают переменные x1...x5.

Формат вывода
Нужно вывести 1000 строк, каждая из которой состоит из одного числа – значения функции в тестовой точки.
Выводить значения в точках нужно в том же порядке, в котором точки тестовой выборки пришли во входном файле.
"""

"""
1.0 2.0 3.9 4.1 5.9 6.1
0.0 5.0 6.9 3.1 4.9 1.1
1.0 2.0 3.9 4.1 5.9 6.1
"""

from sklearn.linear_model import LinearRegression

def main():
    N = 2
    split_symbol = ' '

    # read train data
    x_train = [None] * N
    y_train = [None] * N
    for i in range(0, N):
        arr = input().split(split_symbol)
        x_train[i] = [float(x) for x in arr[:5]]
        y_train[i] = float(arr[5])

    # train classifier
    clf = LinearRegression().fit(x_train, y_train)

    # read test data
    x_test = [None] * N
    for i in range(0, N):
        arr = input().split(split_symbol)
        x_test[i] = [float(x) for x in arr[:5]]

    y_test = clf.predict(x_test)
    for y in y_test:
        print(y)

if __name__ == "__main__":
    main()
