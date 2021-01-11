# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an integer n, find the next biggest integer with 
# the same number of 1-bits on. For example, given the 
# number 6 (0110 in binary), return 9 (1001).

def next_biggest_bin_int(n: int) -> int:
    "Returns the next largest int with the same number of 1s"
    
    # the number of 1s in `n` and n+1
    n_ones, nxt = ("{0:b}".format(n)).count('1'), n+1

    # loop breaks when nxt has the same # of 1s as `n`
    while ("{0:b}".format(nxt)).count('1') != n_ones:
        nxt+=1
    return nxt

if __name__ == "__main__":
    ex = 6
    print(next_biggest_bin_int(ex)) # prints 9