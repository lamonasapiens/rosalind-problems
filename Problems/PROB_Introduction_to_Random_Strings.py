"""Given: A DNA string s of length at most 100 bp and an array A 
containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents
the common logarithm of the probability that a random string constructed
with the GC-content found in A[k] will match s exactly.
_______________________________________________________________________
"""
from math import log10

f = open("datasets/rosalind_prob.txt", "r")
dna, A = f.read().strip().split("\n")
A = list(float(i) for i in A.split())

B = []
for f in A:
    freqs = {
        "G" : f/2,
        "C" : f/2,
        "A" : (1-f)/2,
        "T" : (1-f)/2,
        }
    p = 1
    for i in dna:
        p *= freqs[i]
    B.append(round(log10(p), 4))

print(*B)       