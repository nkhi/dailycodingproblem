# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

# Have a great day!

def pow(a: int, b: int):
    """
    Performs exponentiation, returning a ^ b.
    
    Precondition: Both arguments a and b must be integers.
    """
    # constant
    if a<0:
        a = int(str(a)[1:])
    if b<0:
        b = int(str(b)[1:])
    
    ## faster than multiplication
    return a<<b-1

print(pow(2,3))
print(pow(2,4))
print(pow(2,5))
print(pow(2,6))
print(pow(2,7))
print(pow(2,8))
print(pow(2,10))

# works
print(pow(-2,3))
print(pow(-2,4))
print(pow(-2,5))
print(pow(-2,6))
print(pow(-2,7))
print(pow(-2,8))
print(pow(-2,10))

# all true
print(pow(2,3) == 2**3)
print(pow(2,4) == 2**4)
print(pow(2,5)== 2**5)
print(pow(2,6)== 2**6)
print(pow(2,7)== 2**7)
print(pow(2,8)== 2**8)
print(pow(2,10)== 2**10)