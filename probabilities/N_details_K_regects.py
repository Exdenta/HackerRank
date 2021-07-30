import operator as op
from functools import reduce
import math 

""" Day 4. Binomial Distribution II

A manufacturer of metal pistons finds that, on average, 
12% of the pistons they manufacture are rejected because they are incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:

a) No more than 2 rejects?
b) At least 2 rejects?
"""

def combination(k, n):
    k = min(k, n-k)
    numer = reduce(op.mul, range(n, n-k, -1), 1)
    denom = reduce(op.mul, range(1, k+1), 1)
    return numer / denom   

def get_probability(pistons_count, reject_counts, p_reject):
    P_reject = 0
    for reject_count in reject_counts:
        P_reject += combination(reject_count, pistons_count) * math.pow(p_reject, reject_count) * math.pow(1 - p_reject, pistons_count - reject_count)
    return P_reject

if __name__ == "__main__":
    p_reject = 0.12
    pistons_count = 10

    reject_counts = [0, 1, 2]
    a_prob = get_probability(pistons_count, reject_counts, p_reject)
    print(round(a_prob, 3))

    reject_counts = range(2, pistons_count + 1)
    b_prob = get_probability(pistons_count, reject_counts, p_reject)
    print(round(b_prob, 3))