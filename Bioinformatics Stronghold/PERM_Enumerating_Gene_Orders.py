"""
A permutation of length n is an ordering of the positive integers 
{1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7. Return: The total number of permutations
of length n, followed by a list of all such permutations (in any order).
______________________________________________________________________
"""
from itertools import permutations
from math import factorial


f = open("datasets/rosalind_perm.txt", "r")
n = int(f.read())

numbers = []
for i in range(1, n+1):
    numbers.append(i)

print(factorial(n))
for perm in permutations(numbers):
    print(*perm)