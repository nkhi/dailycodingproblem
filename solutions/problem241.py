from typing import List

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
# It is calculated as follows:

# A researcher has index h if at least h of her N papers have h citations each. 
# If there are multiple h satisfying this formula, the maximum is chosen.

# For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. 
# Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

# Given a list of paper citations of a researcher, calculate their h-index.

def check_h(paper: List, i: int) -> bool:
    "Return true if paper[i] is a valid h-index"
    q = paper[i]
    s = sorted(paper, reverse=True)
    top_q_slice = s[0:q] # top q elements, to check citation amt >= q
    valid_h = [True if x >= q else False for x in top_q_slice]
    return all(valid_h)

def max_h_index(paper: List) -> int:
    "Return a researchers h-index given list paper of the number of citations received on their publications."
    good = []
    for i in range(len(paper)):
        if check_h(paper, i):
            good.append(paper[i])
    return max(good)

if __name__ == "__main__":
    ex = [4, 3, 0, 1, 5]
    print(max_h_index(ex)) # prints 3

    ex2 = [9, 8, 7, 2, 1, 17, 22, 3, 5, 10, 11, 14, 12, 2, 0, 3]
    print(max_h_index(ex2)) # prints 8