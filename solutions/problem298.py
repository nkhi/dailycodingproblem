# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A girl is walking along an apple orchard with a bag in each hand. 
# She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

# Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

# For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.

def n_uniq_elems(arr: list):
    "Return the number of unique elements in list `arr`"

    return len(list(set(arr)))

def longest_slice(trees: list):
    "Return the longest slice from `trees` which has at most 2 elements"

    slice_lens = []
    for i in range(len(trees)):
        for j in range(len(trees)):
            if n_uniq_elems(trees[i:j]) < 3:
                slice_lens.append(len(trees[i:j]))
    return max(slice_lens)
        
if __name__ == "__main__":
  ex = [2, 1, 2, 3, 3, 1, 3, 5]
  ret = longest_slice(ex)
  print(ret) # prints "4"