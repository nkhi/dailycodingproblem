# Good morning! Here's your coding interview problem for today.

# This problem was asked by Yahoo.

# You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

# Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

# For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

def swap(input: str, degree: int):
    "Returns a version of str with the first k chars shifted to the end"
    return input[degree:] + input[:degree]

def lexicographic_min(input: str, degree: int):
    """
    Given a string input, return the minimum possible swaped version.
    """
    # first swap
    a = swap(input, degree)
    store = [a]

    # if single characters, only iterate length-1 # of times
    if degree == 1:
        for i in range(len(input)-1):
            sw = swap(store[-1], degree) # swap the last swapped string
            store.append(sw)
        print(store)
        return(min(store))

    # otherwise, jumps could introduce odd rearrangements so iterate more
    else:
        for n in range(100):
            new = swap(store[-1], degree)
            # print(f"iter:{n}  sw:{sw}")
            store.append(new)
        uniqs = list(set(store)) # remove duplicates
        return(min(uniqs))
    
if __name__ == "__main__":
    example = "daily"
    print(lexicographic_min(example, 1)) # prints ailyd

    example2 = "nikhi"
    print(lexicographic_min(example2, 2)) # prints hinik

    example3 = "manhattan"
    print(lexicographic_min(example3, 4)) # prints anhattanm