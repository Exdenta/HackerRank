import math

def  cumulative_distribution(x, mean, standart_deviation):
    return 0.5 * (1 + math.erf((x - mean) / (standart_deviation * math.sqrt(2))))

if __name__ == "__main__":
    tickets_left = 250
    student_count = 100
    mean = 2.4
    standart_deviation = 2.0

    answer = cumulative_distribution(tickets_left/student_count, mean, standart_deviation)
    print(round(answer, 4))