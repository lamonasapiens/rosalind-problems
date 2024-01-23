"""
Given: An RNA string s of length at most 80 bp having the same number of 
occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in 
the bonding graph of s.
____________________________________________________________________________
"""
from math import factorial

f = open("datasets/rosalind_pmch.txt", "r")
seq = f.read().strip().split("\n", 1)[1].replace("\n", "")

AU_pairs = seq.count("A")
GC_pairs = seq.count("G")

perfect_matchings = factorial(AU_pairs)*factorial(GC_pairs)
print(perfect_matchings)