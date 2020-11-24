from typing import List
# start: 7:45pm
# end: 7:47pm

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# A fixed point in an array is an element whose value is equal to its index. 
# Given a sorted array of distinct elements, return a fixed point, if one exists.
# Otherwise, return False.

# For example, given [-6, 0, 2, 40], you should return 2. 
# Given [1, 5, 7, 8], you should return False.

def get_fixed_point(arr: List) -> int:
    """
    Returns the first fixed point in arr, if one exists.
    Otherwise returns None.
    """
    for i in range(len(arr)):
        if i == arr[i]:
            return arr[i]
    return None


if __name__ == "__main__":
    a = get_fixed_point([-6, 0, 2, 40])
    print(a)