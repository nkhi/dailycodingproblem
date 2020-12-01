from typing import List, Dict

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Two Sigma.

# Ghost is a two-person word game where players alternate appending letters to a word. 
# The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses.
# Here is a sample game:

#     Player 1: g
#     Player 2: h
#     Player 1: o
#     Player 2: s
#     Player 1: t [loses]

# Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

# For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.

def sort_words(words: List) -> List[str]:
    "Returns an ordered dictionary which indicates the first letters, from strings in `words`, which will cause a player to lose a game of ghost."
    key = {0: [], 1: []}

    # Even words win, odd words lose
    for i in words:
        if len(i) % 2 == 1:
            key[0].append(i[0:1])
        else:
            key[1].append(i[0:1])
    return key

def optimal_ghost_opening(key: Dict) -> str:
    "Returns the optimal starting character given the input dictionary key from helper sort_words"

    # overlap is the set of elements which appear in both operands
    overlap = set(key[0]) & set(key[1])

    # return the difference between the winning choices from key[1] and overlap
    # which means thi also supports multiple choice outputs
    return list(set(key[1]).difference(overlap))

if __name__ == "__main__":
    ex = ["cat", "calf", "dog", "bear"]
    q = sort_words(ex)
    e = optimal_ghost_opening(q)
    print(q) # {0: ['c', 'd'], 1: ['c', 'b']}
    print(e) # ['b']