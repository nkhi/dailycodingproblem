# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# You have a large array with most of the elements as zero.

# Use a more space-efficient data structure, SparseArray, that implements the same interface:

#     init(arr, size): initialize with the original large array and size.
#     set(i, val): updates index at i with val.
#     get(i): gets the value at index i.


# Going to convert the input array into a new array where elements are objects or Tuples in this case
# For ex, [0, 1, 0, 0, 0, 2] => [(1, 1), (2, 5)] where the first tuple element is the original value
#                                                and the second is the original index.

class SparseArray:

    def __init__(self, arr: list, size: int):
        "Initalize a new SparseArray"
    
        self.arr = arr or [] # holding a copy of the original for no reason tbh
        self.size = size or 0 # holding the original array size to reconstruct

        # if the element is non-zero, package it into a tuple of the form (value, index)
        self.sparseArr = [(self.arr[x], x) for x in range(len(self.arr)) if self.arr[x] != 0]

        # a flat list of indicies for get()
        self.inds = [i[1] for i in self.sparseArr]

    def set(self, i, val):
        "Set value val at index i"

        new = (val, i)

        # if new value is non-zero
        if val != 0:
            # if the index is full, find the tuple
            # corresponding to that spot and replace
            if i in self.inds:
                for element in self.sparseArr:
                    if element[1] == i:
                        self.sparseArr[i] = new
            
            # otherwise there was previously a 0 there
            else:
                j = 0   # counter
                for ind in self.inds:
                    if ind < i:
                        j+=1
                    elif ind > i:
                        break
                
                # insert new tuple before j+1th element
                self.sparseArr.insert(j+1, new)

                # add index value to the self.inds array
                self.inds.append(i)

        # the new value is 0
        else:
            if i >= self.size:
                self.size+=1

    def get(self, i):

        "Return the value at index i, or 0 otherwise." 
    
        # if requested index is within bounds
        # and registered to a non-zero value
        if i <= self.size and i in self.inds:

            # walk through sparseArr until you find it
            for element in self.sparseArr:
                if element[1] == i:
                    return element[0]

        # otherwise it's not in here, return 0 (should this return -INF?)
        else:
            return 0


if __name__ == "__main__":
    kindOfEmptyArray = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 3, 0, 0, 1, 0]
    betterArray = SparseArray(kindOfEmptyArray, len(kindOfEmptyArray))

    gets = [betterArray.get(i) for i in range(len(kindOfEmptyArray))]
    print(gets == kindOfEmptyArray) # checks if the get() works properly, returns True

    betterArray.set(0, 99999)
    print(betterArray.get(0)) # returns 99999