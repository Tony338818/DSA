"""
Recursion is a function that calls itself repeatedly until it hits a base case.

Use when:
A problem can be broken into smaller versions of the same problem

Use cases:
1. Traversing a tree
2. Searching nested folders
3. Calculating factorials

Requirements
1. Base Case -> When to stop
2. Recursive Case -> Call yourself with a smaller input
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = 3
result = factorial(n=n)
print(result)
