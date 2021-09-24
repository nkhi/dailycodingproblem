# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Given a number represented by a list of digits, find the next greater permutation of a number, 
# in terms of lexicographic ordering. If there is not greater permutation possible,
# return the permutation with the lowest value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. 
# The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

# Can you perform the operation without allocating extra memory (disregarding the input memory)?

from typing import List
from itertools import permutations

def arr_to_int(arr: List[int]) -> int:
    "Converts and returns arr as a single int"

    return int(''.join([str(n) for n in arr]))

def int_to_arr(integer: int) -> List[int]:
    "Convert and returns integer as an array"

    return [int(a) for a in str(integer)]

def get_permutations(arr: List[int]) -> List[int]:
    "Return all permutations of the number represented by the elements of arr"

    return [arr_to_int(out) for out in permutations(arr)]

def get_next_greatest_permutation(arr: List[int]) -> List[int]:
    "Return the next greatest number in terms of lexographic ordering"

    all = sorted(get_permutations(arr))
    next_i = all.index(arr_to_int(arr)) + 1
    next_val = int_to_arr(all[next_i])
    return(next_val)

if __name__ == "__main__":
    test = [1, 2, 3]
    print(get_next_greatest_permutation(test)) # returns [1, 3, 2]