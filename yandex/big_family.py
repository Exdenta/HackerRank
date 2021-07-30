


# https://contest.yandex.ru/contest/28413/problems/C/
#
# У бабушки Алевтины очень большая семья, которая живёт в разных городах. Раньше все члены семьи собирались дома у бабушки Алевтины,
# но в 2020 году было решено, что созваниваться по видеосвязи будет безопаснее для всех. У каждого домохозяйства есть некоторое
# количество комнат с устройствами, при помощи которых можно организовать видео-конференцию на несколько членов семей из других
# городов. Комнаты пользуются большим спросом, так как некоторые члены семьи работают на удалёнке и должны встречаться с коллегами
# по рабочим встречам, поэтому в расписании есть уже занятые слоты. Также все родственники хотят поделиться новостями друг с другом,
# поэтому у всей семьи есть расписание звонков, чтобы каждый участник мог пообщаться в нужное время.
#
# Вам дана информация о доступности комнат во всех домохозяйствах на день встречи членов семей, а также m
# запросов на проведение часовой встречи для родственников из разных городов. Для каждого запроса требуется определить набор подходящих временных слотов (в каждом городе надо выбрать ровно одну комнату, и все эти комнаты должны быть свободны в какой-то час), или сообщить, что подходящего набора нет.
#
# Обратите внимание, запросы независимы друг от друга, то есть, ответ на очередной запрос не влияет на занятость комнат.
#
# --- Формат ввода ---
#
# В первой строке ввода записано число c (2 ≤ c ≤ 16) — количество домохозяйств. Далее следуют c блоков с описанием домохозяйств.
# В первой строке каждого блока записано название города, где расположена часть семьи, и количество комнат в нём ni
# (1 ≤ ni ≤ 100). Далее следуют ni строк, в каждой из которых дано расписание бронирования комнаты tij и его название sij.
# Расписание tij представляет собой строку ровно из 24 символов, k-й символ которой равен ‘X’, если в k-й час суток комната
# недоступна для бронирования, или ‘.’, если доступна.
#
# В следующей строке записано число m (1 ≤ m ≤ 1000) — количество запросов. В каждой из следующих m строк сначала записано число
# l (2 ≤ l ≤ c) — количество городов, в которых должно быть забронировано по одной комнате, а далее записаны l названий городов.
# Названия городов разделены одиночными пробелами.
#
# Названия никаких двух комнат не совпадают. Названия никаких двух городов также не совпадают.
# Названия комнат и городов представляют собой непустые строки, состоящие из букв английского алфавита длиной не более 10 символов.
#
# --- Формат вывода ---
#
# Для каждого из m запросов в отдельной строке выведите сообщение «Yes» (без кавычек) и названия комнаты, в которой можно
# организовать встречу, или выведите сообщение «No» (без кавычек), если подходящую комнату найти невозможно. Комнаты в каждом
# ответе можно выводить в любом порядке. Если возможных ответов на запрос несколько, разрешается вывести любой подходящий.
#
# --- Ввод ---
#
# 3
# Moscow 2
# XXXXXXXX.X.X.X.X.X.XXXXX Kvartal
# XXXXXXXXX.X.X.X.X.X.XXXX Kvartet
# Minsk 1
# XX.XXXXX........XXXXXXXX Toloka
# Berlin 2
# XX..XXXXXXXXXXXXXXXXXXXX Mitte
# XXXXXXXXXXXXXXXX.....XXX Lustgarten
# 4
# 3 Moscow Minsk Berlin
# 2 Moscow Minsk
# 2 Minsk Berlin
# 2 Moscow Berlin
#
# --- Вывод ---
#
# No
# Yes Kvartal Toloka
# Yes Toloka Mitte
# Yes Kvartal Lustgarten
#

class Room:
    room_name: str
    schedule: list # list of 3 ints (24 bits)

    def __init__(self, room_name: str, schedule: list):
        self.room_name = room_name
        self.schedule = schedule

class Household:
    town_name: str
    room_n: int
    rooms: set

    def __init__(self, town_name: str, room_n: int, rooms: list):
        self.town_name = town_name
        self.room_n = room_n
        self.rooms = rooms

def bit2int(bit_arr: str):
    integer = 0
    for i, bit in enumerate(bit_arr):
        integer += pow(2, i) * int(bit)
    return integer

def bit_sequence_to_int_array(bit_sequence: str):
    sequence = list()
    for bit_idx in range(0, len(bit_sequence) // 8):
        integer = bit2int(bit_sequence[bit_idx * 8: (bit_idx + 1) * 8])
        sequence.append(integer)
    return sequence

def get_sequence_with_repetition(values: set, reps: int, sequence_len: int) -> list:
    """
    Returns sequence of length 'sequence_len' where each value repeats 'reps' number of time
    """
    sequence = list()
    iteration_count = (sequence_len // reps) // len(values)
    for i in range(0, iteration_count):
        for value in values:
            for rep_idx in range(0, reps):
                sequence.append(value)
    return sequence

def get_household(households: list, town_name: str):
    for household in households:
        if household.town_name == town_name:
            return household
    return None

def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2

def main():
    n_households = int(input())

    households = list()
    arr_idx = 1
    for i in range(0, n_households):
        town_name, n_room = input().split()
        arr_idx += 1

        rooms = list()
        for _ in range(0, int(n_room)):
            schedule, room_name = input().split()
            schedule = bit_sequence_to_int_array(schedule.replace('X', "0").replace('.', "1"))
            arr_idx += 1
            rooms.append(Room(room_name, schedule))

        households.append(Household(town_name, int(n_room), set(rooms)))

    # check if connections are possible
    n_connections = int(input())
    arr_idx += 1

    result_messages = []
    for input_arr_idx in range(arr_idx, n_connections + arr_idx):
        towns = input().split()[1:]

        variations_n = 1
        for household in households:
            if household.town_name in towns:
                variations_n *= household.room_n

        # get all room variations
        variations = [list()] * len(towns)
        reps_power = 0
        for town_idx, town in enumerate(towns):
            household = get_household(households, town)
            sequence = list()
            if household.room_n == 1:
                # all variations will include only this room
                # so no need for repetitions
                sequence = get_sequence_with_repetition(household.rooms, 1, variations_n)
            else:
                # every next variation should have twice as mush room repetitions
                # to cover all variations
                sequence = get_sequence_with_repetition(household.rooms, pow(2, reps_power), variations_n)
                reps_power += 1

            variations[town_idx] = sequence

        # go through all variations and multiply all schedules in rooms
        # if result >= 0 then there is a window for connection
        success = True
        for variation_idx in range(0, variations_n):
            results = [256] * 3
            for town_idx in range(0, len(towns)):
                for i, n in enumerate(variations[town_idx][variation_idx].schedule):
                    results[i] = results[i] and n
            if sum(results) > 0:
                result_message = "Yes"
                for idx in range(0, len(towns)):
                    result_message += " " + variations[idx][variation_idx].room_name
                result_messages.append(result_message)
                success = True
                break
            else:
                success = False

        if not success:
            result_messages.append("No")

    for message in result_messages:
        print(message)


"""
------------------- Input 1 -------------------------
3
Moscow 2
XXXXXXXX.X.X.X.X.X.XXXXX Kvartal
XXXXXXXXX.X.X.X.X.X.XXXX Kvartet
Minsk 1
XX.XXXXX........XXXXXXXX Toloka
Berlin 2
XX..XXXXXXXXXXXXXXXXXXXX Mitte
XXXXXXXXXXXXXXXX.....XXX Lustgarten
4
3 Moscow Minsk Berlin
2 Moscow Minsk
2 Minsk Berlin
2 Moscow Berlin

------------------- Output 1 -------------------------
No
Yes Kvartal Toloka
Yes Toloka Mitte
Yes Kvartal Lustgarten
"""

"""
------------------- Input 2 -------------------------
3
Moscow 1
XXXXXXXX...........XXXXX Kvartal
Minsk 1
XXXXXXX...........XXXXXX Toloka
Berlin 1
XXXXXX...........XXXXXXX Mitte
1
3 Moscow Minsk Berlin

------------------- Output 2 -------------------------
Yes Kvartal Toloka Mitte
"""

if __name__ == "__main__":
    main()
