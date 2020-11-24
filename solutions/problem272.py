import itertools

# start: 8:20
# end 8:54

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Spotify.

# Write a function, throw_dice(N, faces, total), that determines how many ways 
# it is possible to throw N dice with some number of faces each to get a specific total.

# For example, throw_dice(3, 6, 7) should equal 15.

def throw_dice(N, faces, total) -> int:
    """
    Returns the number of possibile combinations
    of N dice rolls, each with faces faces, totalling total.
    """

    # If total is higher than the highest possible roll
    if total > N*faces:
        return 0

    # get all possible die-face values in a list of lists
    all_sides = sorted([ list(range(1, faces+1)) * N ][0])

    # get all possible combinations of the dice faces
    all_rolls = [ x for x in itertools.combinations(all_sides, 3) ]

    # sum all the possible 'rolls'
    all_totals = [ sum(y) for y in all_rolls ]

    # set up table for easy return
    total_freqs = { v:0 for v in range(1, (N*faces)+1)}
    for x in all_totals:
        total_freqs[x] += 1

    return(total_freqs[total])

if __name__ == "__main__":

    a = throw_dice(3, 6, 7)
    print(a) # 54 ways to roll 7 with three 6-sided dice

    b = throw_dice(1, 6, 7)
    print(b) # 0 ways to roll 7 with one 6-sided dice