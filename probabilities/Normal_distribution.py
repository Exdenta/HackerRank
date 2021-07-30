import math
import matplotlib.pyplot as plt
import numpy as np

""" Day 5: Normal Distribution II

The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. 
If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

1) Scored higher than 80?
2) Passed the test (>=60)?
3) Failed the test (<60)?
"""

def  cumulative_distribution(x, mean, standart_deviation):
    return 0.5 * (1 + math.erf((x - mean) / (standart_deviation * math.sqrt(2))))

if __name__ == "__main__":
    mean, standard_deviation = 70, 10

    task1 = 80
    answer1 = 1 - cumulative_distribution(task1, mean, standard_deviation)

    task2 = 60
    answer2 = 1 - cumulative_distribution(task2, mean, standard_deviation)
    
    answer3 = cumulative_distribution(task2, mean, standard_deviation)

    print(round(answer1 * 100, 3))
    print(round(answer2 * 100, 3))
    print(round(answer3 * 100, 3))

    # X = np.arange(15, 25, 0.25)
    # Y = []
    # for x in X:
    #     Y.append(normal_distributed_probability(x, mean, standard_deviation))
    # plt.plot(X, Y)
    # plt.show()
    