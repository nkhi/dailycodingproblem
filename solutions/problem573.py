# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a stack of N elements, interleave the first half of the stack 
# with the second half reversed using only one other queue. This should be done in-place.

# Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

# Hint: Try working backwards from the end state.

from collections import deque

def interleave(stack):
    queue = deque([])
    l = len(stack)

    # FIRST PASS: add all to queue
    for x in range(l):
        queue.append(stack.pop())

    # SECOND PASS: add first half of stack elems
    # (in rev order) to the stack again
    for x in range(l):
        if x < l//2:
           queue.append(queue.popleft())
        else:
           stack.append(queue.popleft())

    # THIRD PASS: interleave stack elems into
    # queue ordering (queue == i=0, i=N, i=1, i=N-1, ...)
    for x in range(l):
        if x % 2 == 0:
            queue.append(stack.pop())
        else:
            queue.append(queue.popleft())

    # FOURTH PASS: add all elems back to stack
    for x in range(l):
        stack.append(queue.popleft())

stack = [1, 2, 3, 4, 5]
interleave(stack)
print(stack)

secondstack = [1, 2, 3, 4]
interleave(secondstack)
print(secondstack)