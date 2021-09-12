"""
Figurine collection
https://contest.yandex.ru/contest/28413/problems/D/

Петя приехал в экзотическую страну и решил купить памятный сувенир. В сувенирной лавке в ряд выставлены
n статуэток различных видов, причем статуэтка вида t стоит ровно t единиц местной валюты.
Петя решил купить статуэтки всех видов от 1 до k. Оказалось, что Петя получит приличную скидку,
если купит статуэтки, стоящие не в произвольных местах, а некоторым непрерывным отрезком
(все статуэтки от какой-то позиции l до r включительно). Петя сразу понял, что ему может потребоваться
купить несколько статуэток одного вида, повторяющиеся он решил подарить друзьям после возвращения домой.

Например, если в лавке статуэтки выставлены в порядке 1 2 2 3 3 1, и Петя хочет купить статуэтки видов от 1 до 3,
то он может купить статуэтки с первой по четвертую позиции (при этом будут куплены две статуэтки вида 2).
Если же в лавке выставлены статуэтки 1 2 5 4 3 (вновь k = 3), то Петя купит все 5 статуэток.
Помогите определить Пете минимальную суммарную стоимость статуэток, расположенных подряд в лавке, чтобы среди них
были статуэтки всех видов от 1 до k. Гарантируется, что для всех тестовых данных ответ существует.

Формат ввода
В первой строке записаны два целых числа n и k (1 ≤ k ≤ n ≤ 500000).
Во второй сроке записаны n целых чисел ai (вид i-й статуэтки) (1 ≤ ai ≤ n) — описания статуэток в сувенирной лавке.
Статуэтки перечислены слева направо. Гарантируется, что для всех тестовых данных ответ существует.

Формат вывода
Выведите одно целое число — минимальную сумму в местной валюте, за которую мог бы купить статуэтки Петя
(без учета будущей скидки).
"""

"""
---------- Input ---------
6 3
1 2 2 3 3 1
---------- Output ---------
8
"""

def minimal_cost(n, k, figurines):
    """
    Naive algorithm
    """

    # list of all figurines to buy
    figurines_to_buy = [x for x in range(1, k + 1)]
    figurines_to_buy_len = len(figurines_to_buy)
    figurines_bought = [0] * (figurines_to_buy_len + 1)

    minimal_sum = 2147483647
    for i, figurine in enumerate(figurines):
        if figurine == 1:
            # get left sum
            sum_temp = 0
            for fig_idx in range(0, figurines_to_buy_len):
                figurines_bought[fig_idx] = 0

            for left_i in range(i, 0, -1):
                current_figurine = figurines[left_i]
                sum_temp += current_figurine
                if current_figurine <= k:
                    if figurines_bought[current_figurine] == 0:
                        figurines_bought[current_figurine] = 1

                if current_figurine == k:
                    if sum(figurines_bought) == figurines_to_buy_len:
                        if minimal_sum > sum_temp:
                            minimal_sum = sum_temp
                        break

            # get right sum
            sum_temp = 0
            for fig_idx in range(0, figurines_to_buy_len):
                figurines_bought[fig_idx] = 0
            
            for right_i in range(i, len(figurines), 1):
                current_figurine = figurines[right_i]
                sum_temp += current_figurine
                if current_figurine <= k:
                    if figurines_bought[current_figurine] == 0:
                        figurines_bought[current_figurine] = 1

                if current_figurine == k:
                    if sum(figurines_bought) == figurines_to_buy_len:
                        if minimal_sum > sum_temp:
                            minimal_sum = sum_temp
                        break


    return minimal_sum


def main():
    n, k = [int(x) for x in input().split()]
    figurines = [int(x) for x in input().split()]
    cost = minimal_cost(n, k, figurines)
    print(cost)

if __name__ == "__main__":
    main()
