"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).

A transition substitutes one purine for another (A↔G) or one pyrimidine for another (C↔T)
A transversion is the interchange of a purine for a pyrimidine base, or vice-versa.
_________________________________________________________________________________________
"""

f = open("datasets/rosalind_tran.txt", "r")
fasta = f.read().strip().split(">")

s1 = fasta[1].split("\n", 1)[1].replace("\n", "")
s2 = fasta[2].split("\n", 1)[1].replace("\n", "")

purines = ["A", "G"]
pyrimidines = ["T", "C"]

transitions = 0
transversions = 0

for i, j in zip(s1,s2):
    if i!= j:
        if i in purines and j in purines:
            transitions += 1
        elif i in pyrimidines and j in pyrimidines:
            transitions += 1
        else:
            transversions += 1

ratio = transitions / transversions
print(ratio)