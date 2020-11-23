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

    # if the length isnt a multiple of 8, the
    # string is malformed
    if n != int(n):
        return False

    # n is an int
    n = int(n)

    # single byte case
    if n==1 and input[0] == 0:
        return True

    # n-byte case
    else:
        first_n_bytes = input[0:n]
        other_first_bytes = []

        # step every 8 chats and get byte i's first char
        i = 1
        while i != n:
            start = 8*i
            stop = start + 2
            other_first_bytes.append(1 if input[start:stop] == [1, 0] else 0)
            i+=1
        
        # if first n bytes are all 1 and other n-1 bytes start with 10s
        if all(first_n_bytes) and all(other_first_bytes):
            return True

    # anything else
    return False

if __name__ == "__main__":
    example = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0 ,1, 0, 1, 0, 1,1, 0, 0]
    ret = is_valid_utf(example)
    print(f"{''.join([str(elem) for elem in example])} is {'a valid UTF-8 string' if ret else 'is malformed'}")
