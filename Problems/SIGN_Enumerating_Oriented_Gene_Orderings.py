"""
Given: A positive integer n≤6.
Return: The total number of signed permutations of length n, followed
by a list of all such permutations (you may list the signed permutations 
in any order).
______________________________________________________________________________
"""
from itertools import permutations
from math import factorial

f = open("datasets/rosalind_sign.txt", "r")
n = f.read().strip()
n = int(n)

numbers = list(i for i in range(-n, n+1))
numbers.remove(0)

print(factorial(n)*(2**n))
for perm in permutations(numbers, n):
    positive_perm = [abs(i) for i in perm]
    if all(positive_perm.count(i) == 1 for i in positive_perm):
        print(*perm) 