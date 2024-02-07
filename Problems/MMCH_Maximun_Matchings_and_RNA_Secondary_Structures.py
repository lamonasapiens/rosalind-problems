"""
Given: An RNA string s of length at most 100.
Return: The total possible number of maximum matchings of basepair edges in the 
bonding graph of s.
________________________________________________________________________________
"""
from collections import Counter
from math import factorial

f = open("datasets/rosalind_mmch.txt", "r")
seq = f.read().strip().split("\n", 1)[1].replace("\n","")

bases = Counter(seq)
AU_pairs = min(bases["A"], bases["U"])
CG_pairs = min(bases["C"], bases["G"])

maxAU = max(bases["A"], bases["U"])
maxCG = max(bases["C"], bases["G"])

def per(n,k):
    return factorial(n)//factorial(n-k)


"""The formula is the same as in "Perfect Matchings": Factorial(AU_pairs) * Factorial(CG_pairs).
However, instead of factorials we use permutations, where n= the base with higher count and
k=nº of base-pairs"""
matchings = per(maxAU, AU_pairs) * per(maxCG, CG_pairs)

print(matchings)