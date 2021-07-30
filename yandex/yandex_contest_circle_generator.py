# %%

from tqdm import tqdm
import numpy as np
import math
import matplotlib.pyplot as plt
import random

# Петя написал два генератора точек в круге:


def generate1():
    a = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    return (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))


def generate2():
    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)


# Даны 100 наборов по 1000 точек, каждый набор сгенерирован каким-то одним из этих двух алгоритмов. Необходимо определить для каждого набора, первый или второй алгоритм использовался для его генерации.
# Для того, чтобы получить ОК по этой задаче, надо предсказать правильный генератор хотя бы для 98 наборов.

#
# Solution:
#

outputs = []
for i in range(0, 100):
    arr = input().split()
    outputs.append(sum([abs(float(x)) for x in arr]))

for i in range(0, 100):
    if outputs[i] > 742.69:
        print(2)
    else:
        print(1)

#
# ------------------- Tests -------------------
#

# %%


def generate():
    gen1_x = []
    gen1_y = []
    gen2_x = []
    gen2_y = []
    for i in range(0, 1000):

        x, y = generate1()
        gen1_x.append(x)
        gen1_y.append(y)

        x, y = generate2()
        gen2_x.append(x)
        gen2_y.append(y)

    return (gen1_x, gen1_y, gen2_x, gen2_y)


gen1_x, gen1_y, gen2_x, gen2_y = generate()

# %%

plt.plot(gen1_x, gen1_y, '.')
plt.show()

# %%
plt.plot(gen2_x, gen2_y, '.')
plt.show()

# %%

gen1_x, gen1_y, gen2_x, gen2_y = generate()

hist_gen1 = np.zeros((100), dtype=np.int)
for x in gen1_x:
    hist_gen1[int((x + 1) * 100/2)] += 1

print("hist_gen1: ", hist_gen1)
print("gen1 half sum: ", np.sum([max(0, x) for x in gen1_x]))

hist_gen2 = np.zeros((100), dtype=np.int)
for x in gen2_x:
    hist_gen2[int((x + 1) * 100/2)] += 1

print("hist_gen2: ", hist_gen2)
print("gen2 half sum: ", np.sum([max(0, x) for x in gen2_x]))

# %%


# figure out threshold for generators

sums1_x = []
sums1_y = []
sums2_x = []
sums2_y = []

for i in tqdm(range(0, 10000)):
    gen1_x, gen1_y, gen2_x, gen2_y = generate()

    sums1_x.append(np.sum([max(0, x) for x in gen1_x]))
    sums1_y.append(np.sum([max(0, x) for x in gen1_y]))
    sums2_x.append(np.sum([max(0, x) for x in gen2_x]))
    sums2_y.append(np.sum([max(0, x) for x in gen2_y]))


# %%

plt.plot(sums1_x, sums1_y, '.')
plt.show()

plt.plot(sums2_x, sums2_y, '.')
plt.show()

# %%

print("1 for x. max: ", np.max(sums1_x), ", min: ",
      np.min(sums1_x), ", mean: ", np.mean(sums1_x))
print("1 for y. max: ", np.max(sums1_y), ", min: ",
      np.min(sums1_y), ", mean: ", np.mean(sums1_y))
print("2 for x. max: ", np.max(sums2_x), ", min: ",
      np.min(sums2_x), ", mean: ", np.mean(sums2_x))
print("2 for y. max: ", np.max(sums2_y), ", min: ",
      np.min(sums2_y), ", mean: ", np.mean(sums2_y))

# %%
len(sums1_x)
# %%

mean_1 = np.mean(sums1_x)
std_1 = math.sqrt(np.sum([math.pow(x - mean_1, 2)
                  for x in sums1_x])/len(sums1_x))
conf_interv = 3.291 * std_1 / \
    math.sqrt(len(sums1_x))  # 3.291 - 99.9% confidence
print("mean: ", mean_1)
print("std: ", std_1)
print("confidence interval: ", conf_interv)


# %%

threshold_x = (np.mean(sums2_x) + np.mean(sums1_x)) / 2
print(threshold_x)

# %%


def generate():
    gen1 = []
    gen2 = []
    for i in range(0, 1000):

        x, y = generate1()
        gen1.append(x)
        gen1.append(y)

        x, y = generate2()
        gen2.append(x)
        gen2.append(y)

    return (gen1, gen2)


gen1, gen2 = generate()

# %%

N = 10000
sums1 = np.zeros(N)
sums2 = np.zeros(N)

for i in tqdm(range(0, N)):
    gen1, gen2 = generate()
    sums1[i] = np.sum([abs(x) for x in gen1])
    sums2[i] = np.sum([abs(x) for x in gen2])

print("sums1 mean: ", np.mean(sums1))
print("sums2 mean: ", np.mean(sums2))

# %%

print("sums1 mean: ", np.mean(sums1))
print("sums2 mean: ", np.mean(sums2))
print((np.mean(sums1) + np.mean(sums2)) / 2)  # = 742.69

# %%
