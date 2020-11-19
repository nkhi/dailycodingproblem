# Good morning! Here's your coding interview problem for today.

# This problem was asked by Mailchimp.

# You are given an array representing the heights of neighboring buildings on a city street, from east to west. 
# The city assessor would like you to write an algorithm that returns how many of these buildings have a view 
# of the setting sun, in order to properly value the street.

# For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings 
# with heights 8, 6, and 1 all have an unobstructed view to the west.

# Can you do this using just one forward pass through the array?

# my interpretation: need to check if position 'i' is greater than position 'i+1'
#                    of some given array of integers.

def n_sunset_view(buildings):
    """
    Return the number of buildings with heights represented in int array 'buildings' 
    which have a view of the sun setting in the west.    
    """
    count = 0
    for i in range(len(buildings)-1):
        if buildings[i] > buildings[i+1]:
            count+=1
    return(count+1)

if __name__ == "__main__":
    print('write something')
    a = input()
    print(a)
    print(n_sunset_view(example_array))
    # output: 3