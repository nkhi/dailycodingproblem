# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Implement an efficient string matching algorithm.

# That is, given a string of length N and a pattern of length k, 
# write a program that searches for the pattern in the string with 
# less than O(N * k) worst-case time complexity.

# If the pattern is found, return the start index of its location.
# If not, return False.

def search(pattern: str, target: str) -> bool:
    """
    Returns True if pattern occurs within target.
    Otherwise returns False.
    Assumptions: len(pattern) < len(target)
    """
    # N
    for i in range(len(target)):
        # whatever i ends up being, worst case i = n
        while i < len(target):
            chunk = target[i:i+len(pattern)] # unnecessary, just to see iterations
            print(chunk)
            if chunk == pattern:
                return True
            i += 1
    x = target[-2:] == pattern

    # O(N * i) + 1 ?< O(N * k)
    return x or False

if __name__ == "__main__":
    a = search("ik", "nikhi") # i iterates twice, so 3 iterations < 5*2 iterations
    print(a) #True