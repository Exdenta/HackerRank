
""" Day 4: Geometric Distribution II

The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1-st defect is found during the first 5 inspections?
"""

if __name__ == "__main__":
    probability = 1/3
    N = 5

    P = 0
    for n in range(1, N + 1):
        p = 1
        for i in range(1, n):
            p *= 1 - probability
        p *= probability
        print(f"p: {p}")
        P += p
    
    print(round(P, 3))
