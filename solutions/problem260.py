from typing import List

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Pinterest.

# The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. 
# Given this information, reconstruct an array that is consistent with it. 
# For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].

# What a funny question

def walk_list(fluxes: List) -> List[int]:
    """
    Return a list of ints which is in an order denoted by the 
    element-wise sign relative to it's predecessor given in `fluxes`
    Assumes fluxes[0] is None

    >>> walk_list([None, +, +, -, +])
    [1, 2, 3, 0, 4]
    """

    i, nums = 1, []
    for flux in fluxes:

        # First element appends 1 to the list nums
        if flux is None:
            nums.append(i)

        # Then all subsequent elements append
        # max(nums)+1 or min(nums)+1 starting at 1
        elif flux == '+':
            nums.append(max(nums)+1)

        elif flux == '-':
            nums.append(min(nums)-1)
    
    # Return sequence
    return nums

if __name__ == "__main__":
    ex = [None, '+', '+', '-', '+']
    print(walk_list(ex)) # 1, 2, 3, 0, 4

    ex2 = [None, '-', '-', '-', '-', '-', '+', '+', '+']
    print(walk_list(ex2)) # 1, 0, -1, -2, -3, -4, 2, 3, 4