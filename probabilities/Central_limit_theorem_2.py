import math

def  cumulative_distribution(x, mean, standart_deviation):
    return 0.5 * (1 + math.erf((x - mean) / (standart_deviation * math.sqrt(2))))

if __name__ == "__main__":
    sample_count = 100
    mean = 500
    standard_deviation = 80
    probability = 0.95
    z_score = 1.96

    mean_new = mean
    standard_deviation_new = standard_deviation / math.sqrt(sample_count)

    answer1 = (mean_new - z_score * standard_deviation_new)
    answer2 = (mean_new + z_score * standard_deviation_new)

    print(round(answer1, 2))
    print(round(answer2, 2))

    A = cumulative_distribution(answer1, mean_new, standard_deviation_new)
    B = cumulative_distribution(answer2, mean_new, standard_deviation_new)
    print("B: ", B, ", A: ", A, "B-A: ", B-A)