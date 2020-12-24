from typing import List

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Spotify.

# You are the technical director of WSPT radio, serving listeners nationwide. 
# For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).

# Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, 
#   determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

# For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. 
# In this case the minimum range would be 5, since that would be required for 
#   the tower at position 15 to reach the listener at position 20.

def get_min_range(listeners: list, towers: list) -> int:
    "Return the minimum broadcast range to reach all listeners from towers"
    dists = []
    a = sorted(listeners + towers)
    for i in range(len(a)):
        if a[i] in towers and (i != 0 and i != len(a)-1):
            r_to_l = a[i+1] - a[i]
            l_to_r = a[i] - a[i-1]
            dist = max(r_to_l, l_to_r)
            dists.append(dist)
    return(max(dists))

if __name__ == "__main__": 
    towers = [4, 8, 15]
    people = [1, 5, 11, 20]
    print(get_min_range(people, towers)) # prints 5

    towers2 = [1, 9]
    people2 = [3, 4, 5]
    print(get_min_range(people2, towers2))