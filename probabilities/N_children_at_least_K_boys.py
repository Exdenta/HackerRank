import operator as op
from functools import reduce
import math 

""" Day 4. Binomial Distribution I

The ratio of boys to girls for babies born in Russia is 1.09 to 1. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. 
Then print your result, rounded to a scale of 3 decimal places (i.e., 0.1234 format).
"""

def combination(k, n):
    k = min(k, n-k)
    numer = reduce(op.mul, range(n, n-k, -1), 1)
    denom = reduce(op.mul, range(1, k+1), 1)
    return numer / denom   

if __name__ == "__main__":
    p_boy, p_girl = 1.09/2.09, 1/2.09
    children_count = 6
    boys_counts = [3, 4, 5, 6]

    P_boy = 0
    for boy_count in boys_counts :
        P_boy += combination(boy_count, children_count) * math.pow(p_boy, boy_count) * math.pow(p_girl, children_count - boy_count)

    print(round(P_boy, 3))