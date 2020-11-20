from typing import List
import itertools

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Netflix.

# Given an array of integers, determine whether it contains a Pythagorean triplet. 
# Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

# Interpretation: Of an array of generic size, return a boolean if any 3 integers within
#                  that list are a valid Pythagorean triplet. 

def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    "Returns True if a^2 + b^2 = c^2, otherwise returns False."
    return True if a**2 + b**2 == c **2 else False

def contains_pythagorean_triplet(arr: List[int]) -> bool:
    """
    Returns True if any three numbers in List arr form a valid Pythagorean Triplet, 
    otherwise returns False.
    """
    # Cant be a triple with 2 elements
    if len(arr) < 3:
        return False

    # Get all permutations of the input list with 3 elements
    all_permutations_of_arr = list(itertools.permutations(arr, 3))
    check = False

    # Check each permuted triple using helper fxn
    for p in all_permutations_of_arr:
        if is_pythagorean_triplet(p[0], p[1], p[2]):
            check = True
            break

    # If the loop is never broken, none of the perms are valid
    return check
    
if __name__ == "__main__":
    example = is_pythagorean_triplet(5,12,13)
    print(f"Is 5, 12, 13 a Pythagorean Triplet?: {example}") # True

    example_arr = [5, 12, 13, 14, 2, 9, 1, 8] # Contains 5, 12, 13 so should be true
    example2 = contains_pythagorean_triplet(example_arr)
    print(example2) # True
