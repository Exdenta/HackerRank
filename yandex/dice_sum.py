
'''
Тренировочный контест: машинное обучение
B. Сумма на гранях https://contest.yandex.ru/contest/28413/problems/B/

Вася взял игральную кость и написал на гранях числа a1, a2, a3, a4, a5 и a6.
Для генерации случайного числа Вася решил воспользоваться следующим алгоритмом:
1. Выбрать число k.
2. Подбросить кубик k раз и записать на листик последовательно выпавших чисел bj.
3. ройтись по списку с конца и вычеркнуть число bj, если оно равно bj−1 (b1 всегда останется в последовательности).
Определите математическое ожидание суммы оставшихся в последовательности чисел, если Вася сообщит вам числа ai и k.
Обратите внимание, что кубик у Васи честный и все выпадение любой из граней равновероятно. Кроме этого, подбрасывания кубика независимы.

Examples:
1)
dice_outcomes = [1, 2, 3, 4, 5, 6]
n_outcomes = 2
result = 6.4166666667
2)
dice_outcomes = [1, 1, 1, 1, 1, 1]
n_outcomes = 3
result = 1.000
3)
dice_outcomes = [1, 2, 1, 2, 2, 2]
n_outcomes = 2
result = 2.3333333333
'''


def get_dice_outcomes_probabilities(dice_outcomes: list) -> list:
    '''
    Get list of all outcomes probabilities
    '''
    probs = dict()
    icrement = 1 / len(dice_outcomes)
    for outcome in dice_outcomes:
        if outcome not in probs:
            probs[outcome] = icrement
        else:
            probs[outcome] += icrement
    return probs


def get_all_possible_combinations(outcomes_probs: dict, combination_len: int) -> list:
    '''
    get all possible dice combinations given a combination length
    and all the possible dice outcomes
    '''
    # edge case:
    if len(outcomes_probs) == 1:
        return [[list(outcomes_probs.keys())[0]]]

    n_combinations = pow(len(outcomes_probs), combination_len)
    combinations = [[None] * n_combinations] * combination_len

    for row in range(0, combination_len):

        # outcome combination
        combination = [None] * n_combinations

        # number of repetitions of each
        # outcome in the combination
        repeat_count = pow(2, row)

        col = 0
        # repeat extra times to fill combination
        for _ in range(0, (n_combinations // repeat_count) // len(outcomes_probs)):

            # repeat every unique dice outcome repeat_count times
            for dice_value in outcomes_probs.keys():
                for _ in range(0, repeat_count):
                    combination[col] = dice_value
                    col += 1

        combinations[row] = combination

    # transpose, so we have combinations
    return list(map(list, zip(*combinations)))


def count_combinations_probabilities(combinations: list, dice_outcomes_probs: dict) -> list:
    '''
    count probability of every combination
    '''
    combinations_probs = [1] * len(combinations)

    for comb_idx, combination in enumerate(combinations):
        for n in combination:
            combinations_probs[comb_idx] *= dice_outcomes_probs[n]

    return combinations_probs


def count_combinations_sums(combinations: list):
    '''
    count combinations sums, where we got rid of all
    neighbouring repeating numbers
    '''

    sums = [0] * len(combinations)

    for comb_idx, combination in enumerate(combinations):

        # add first one
        sums[comb_idx] += combination[0]
        last_added_n = combination[0]

        # add all non repeating
        for n in combination:
            if last_added_n != n:
                sums[comb_idx] += n
                last_added_n = n

    return sums


def get_median_sum(sums: list, sum_probs: list):
    '''
    get median sum, taking into account sum's probability
    '''
    assert(len(sums) == len(sum_probs))
    return sum([sums[i] * sum_probs[i] for i in range(0, len(sums))])


if __name__ == "__main__":
    dice_outcomes = [1, 2, 1, 2, 2, 2]
    n_outcomes = 2

    outcomes_probs = get_dice_outcomes_probabilities(dice_outcomes)
    combinations = get_all_possible_combinations(outcomes_probs, n_outcomes)
    combinations_probs = count_combinations_probabilities(
        combinations, outcomes_probs)
    combinations_sums = count_combinations_sums(combinations)
    median_sum = get_median_sum(combinations_sums, combinations_probs)

    print(median_sum)
    assert median_sum != 2.3333333333
