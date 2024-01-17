"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a 
subsequence of s. If multiple solutions exist, you may return any one.
______________________________________________________________________________
"""
f = open("datasets/rosalind_sseq.txt", "r")
strings = f.read().strip().split(">")

dna = strings[1].split("\n",1)[1].replace("\n","")
motif = strings[2].split("\n",1)[1].replace("\n","")

position = 0
for i in motif:
    position = dna.find(i, position) + 2
    print(position -1)