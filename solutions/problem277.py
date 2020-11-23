from typing import List

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

# For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

#     For a single-byte character, the first bit must be zero.
#     For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.

# Visually, this can be represented as follows.

#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.

def is_valid_utf(input: List[int]) -> bool:
    """
    Returns True if `input` has a valid UTF-8 encoding:
        For a single-byte character, the first bit must be zero.
        For an n-byte character, the first byte starts with n ones and a zero. 
            The other n - 1 bytes all start with 10.
    Otherwise returns False.
    """

    n = len(input) / 8
# 2 9
# 3 17
# 4 25
    print(n)
    if n != int(n):
        return False

    n = int(n)
    print(n)

    if n==1 and input[0] == 0:
        return True

    else:
        first_n_bytes = input[0:n]
        i = 1
        other_first_bytes = []
        while i != n:
            start = 8*i
            stop = start + 1
            other_first_bytes.append(input[start:stop])
            i+=1
        if all(first_n_bytes) and all(other_first_bytes):
            return True

    return False

if __name__ == "__main__":
    example = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0 ,1, 0, 1, 0, 1,1, 0, 0]
    ret = is_valid_utf(example)
    print(ret)
