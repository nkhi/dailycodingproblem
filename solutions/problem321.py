from math import sqrt
from functools import reduce

# Good morning! Here's your coding interview problem for today.

# This problem was asked by PagerDuty.

# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

#     You may decrement N to N - 1.
#     If a * b = N, you may decrement N to the larger of a and b.

# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

# Copied from SO, because this needs to be efficient
# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    step = 2 if n%2 else 1
    f = [[i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0]
    f.pop(0)
    return f

def num_steps(n: int) -> int:
    "Return the minimum number of steps from n to 1"

    x, c = sorted(list(range(1, n+1)), reverse=True), 0
    curr = x[0]
    while curr != 1:
        c += 1
        f = factors(curr)
        next_move = curr - 1
        nxt = curr - 1
        mnm = 9000000
        for x in f:
            mnm = min(x[0], x[1], nxt)
        print(f"curr {curr} c {c}")
        curr = min(nxt, mnm)
        print(f"next {curr}")
    return c

if __name__ == "__main__":
    ex = 12
    sol = num_steps(ex)
    print(f"seed: {ex} number of steps: {sol}")
    # seed: 12 number of steps: 3

    ex2 = 50
    sol2 = num_steps(ex2)
    print(f"seed: {ex2} number of steps: {sol2}")
    # seed: 50 number of steps: 4

    ex3 = 319
    sol3 = num_steps(ex3)
    print(f"seed: {ex3} number of steps: {sol3}")
    # seed: 12 number of steps: 4

    ex4 = 9812
    sol4 = num_steps(ex4)
    print(f"seed: {ex4} number of steps: {sol4}")
    # seed: 12 number of steps: 4
    