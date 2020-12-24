from typing import List
import numpy as np

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

# Here is an example:

# 1 2 3 4 8
# 5 1 2 3 4
# 4 5 1 2 3
# 7 4 5 1 2
# Write a program to determine whether a given input is a Toeplitz matrix.

def is_toepliz(mat: List, mode=0) -> bool:
    "Return if matrix `mat` is a valid Topelitz matrix"

    if not mode:
        # turn any input list of lists into a numpy array
        m = np.array([row for row in mat])

        # get shape
        h, w = m.shape

        # get a list of all diagonals, no wasted loops
        diags = [list(np.diag(m, k=n)) for n in range(-h+1, w)]

        # booleans repr if the diagonal was constant
        constant_diags = [np.all(arr == arr[0]) for arr in diags]

        return all(constant_diags)

    # todo: implementation without numpy
    else:
        h, w = list(sorted(range(len(mat)), reverse=True)), list(range(len(mat[0])))
        horizontal_count = 0
        for i in h:
            while horizontal_count > -1:
                print(mat[i][horizontal_count])
                horizontal_count -= 1
            horizontal_count += 1
            # # only check h_ind 0

            # while w_ind > -1:
                
            #     print(mat[i][w_ind])
            #     w_ind-=1
            # w_ind = 0
            
            # print(mat[hcount][wcount])

        # print(hcount, wcount)
        # diags = []
        return True

if __name__ == "__main__":
    ex = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    print(is_toepliz(ex)) # False, correct

    given_ex = [[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2]]
    print(is_toepliz(given_ex)) # True, correct

    # without numpy implementations
    print(is_toepliz(ex, mode=1))
    print(is_toepliz(given_ex, mode=1))