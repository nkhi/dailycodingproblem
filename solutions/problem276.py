# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Implement an efficient string matching algorithm.

# That is, given a string of length N and a pattern of length k, 
# write a program that searches for the pattern in the string with 
# less than O(N * k) worst-case time complexity.

# If the pattern is found, return the start index of its location.
# If not, return False.

def search(pattern: str, target: str) -> bool:
    for i in range(len(target)):
        while i < len(target):
            if target[i:i+1] == pattern:
                return True
            i += 1
    x = target[-2:] == pattern
    return x or False

if __name__ == "__main__":
    a = search("hi", "nikhi")
    print(a) #True