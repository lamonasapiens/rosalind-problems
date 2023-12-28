"""
Given: A collection of at most 10 symbols defining an ordered
alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the 
nglish alphabet).
_____________________________________________________________________
"""
from itertools import product

f = open("datasets/rosalind_lexf.txt", "r")
symbols, n = f.readlines()

n = int(n)
symbols = symbols.split()

for seq in product(symbols, repeat = n):
    print(*seq, sep="")