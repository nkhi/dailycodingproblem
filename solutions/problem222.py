# This problem was asked by Quora.

# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

def reduce_pathname(inp: str) -> str:
    "Given a valid path location inp, return the shortest standardized path"

    # split into tokens between slashes, remove first and last empty strs
    l = inp.split('/')[1:]
    n = [''] # to get preceding slash

    for i in range(len(l)-1):
        # do not append if current elem is . or .. or next elem is ..
        if l[i+1] == '..' or l[i] == '..' or l[i] == '.':
            pass
        elif l[i+1] == '.':
            n.append(l[i])
        else:
            n.append(l[i])
    
    # to get trailing slash
    n.append('')
    
    # return simplified token list with / as seperator
    return '/'.join(n)

if __name__ == "__main__":
    example = "/usr/bin/../bin/./scripts/../"
    print(reduce_pathname(example)) # prints /usr/bin

    ex2 = "/home/nikhi/../nikhi/./././Projects/../Desktop/dailycodingproblems/./././solutions/../"
    print(reduce_pathname(ex2)) # prints /home/nikhi/Desktop/dailycodingproblems/