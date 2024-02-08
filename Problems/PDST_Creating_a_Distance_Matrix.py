"""
Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). 
Strings are given in FASTA format.

Return: The matrix corresponding to the p-distance on the given strings. As always, 
note that your answer is allowed an absolute error of 0.001.

The p-distance between s1 and s2 is is the proportion of corresponding symbols that 
differ between s1 and s2
__________________________________________________________________________________
"""
f = open("datasets/rosalind_pdst.txt", "r")

seqs = f.read().strip().split(">")[1:]
seqs = [seq.split("\n",1)[1].replace("\n","") for seq in seqs]

def distance(s1, s2):
    mutations = 0
    for i,j in zip(s1,s2):
        if i != j:
            mutations += 1
    p = round(mutations/len(s1), 5)
    return f"{p:.5f}"

n = len(seqs)
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = distance(seqs[i],seqs[j])

for m in matrix:
    print(*m)