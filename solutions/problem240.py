import random

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Spotify.

# There are N couples sitting in a row of length 2 * N. 
# They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.

# What is the minimum number of swaps necessary for this to happen?

# Interpretation: This is a sorting question, where I need to find the best-case scenario for many sorting algos with random array 
# I will implement Quicksort, the fastest heap algorithm I have memorized and then I will run various tests to see what the min number
# of swaps required. I will also assume for simplicity that each person in the row can be denoted by an int, and that couples are n,n+1 respectively

# Answer: The minimum number of swaps is between (min=2N, avg=2Nlog(2N), max=(2N)^2) inclusive, where N is the number of couples.

# Quicksort

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            # print(f"SWAP {arr[j]} and {arr[i]}") uncomment to see swaps in console

            # unpythonic way of keeping a counter
            global iters
            iters += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# global 'swap' counter var
iters = 0

if __name__ == "__main__":
    trials = []
    for n in range(20):
        top = random.randint(50, 120)
        couples = list(range(top))
        random.shuffle(couples)
        quickSort(couples, 0, len(couples)-1)
        trials.append(f"iters: {iters}, elems: {len(couples)}, approx. {iters / len(couples)} swaps per elem")
    
    for i in trials:
        print(i)

    # Sample Output (swaps/element between ~3 and ~100 depending on randomization)
    # iters: 305, elems: 96, approx. 3.1770833333333335 swaps per elem (OR 3n)
    # iters: 542, elems: 81, approx. 6.691358024691358 swaps per elem (OR 6.7n)
    # iters: 864, elems: 91, approx. 9.494505494505495 swaps per elem (etc)
    # iters: 1145, elems: 102, approx. 11.22549019607843 swaps per elem
    # iters: 1468, elems: 102, approx. 14.392156862745098 swaps per elem
    # iters: 1742, elems: 92, approx. 18.934782608695652 swaps per elem
    # iters: 1921, elems: 73, approx. 26.315068493150687 swaps per elem
    # iters: 2048, elems: 58, approx. 35.310344827586206 swaps per elem
    # iters: 2377, elems: 107, approx. 22.214953271028037 swaps per elem
    # iters: 2703, elems: 95, approx. 28.45263157894737 swaps per elem
    # iters: 2970, elems: 73, approx. 40.68493150684932 swaps per elem
    # iters: 3355, elems: 87, approx. 38.5632183908046 swaps per elem
    # iters: 3764, elems: 98, approx. 38.40816326530612 swaps per elem
    # iters: 3968, elems: 67, approx. 59.223880597014926 swaps per elem
    # iters: 4333, elems: 108, approx. 40.120370370370374 swaps per elem
    # iters: 4695, elems: 98, approx. 47.90816326530612 swaps per elem
    # iters: 4972, elems: 73, approx. 68.10958904109589 swaps per elem
    # iters: 5083, elems: 51, approx. 99.66666666666667 swaps per elem
    # iters: 5446, elems: 108, approx. 50.425925925925924 swaps per elem
    # iters: 5836, elems: 112, approx. 52.107142857142854 swaps per elem
