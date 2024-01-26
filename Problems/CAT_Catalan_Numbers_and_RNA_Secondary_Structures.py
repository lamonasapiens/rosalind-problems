"""
Given: An RNA string s having the same number of occurrences of 'A' as 'U'
and the same number of occurrences of 'C' as 'G'. The length of the string is
at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges 
in the bonding graph of s, modulo 1,000,000.
"""

f = open("datasets/rosalind_cat.txt", "r")
seq = f.read().strip().split("\n", 1)[1].replace("\n", "")

def valid_seq(rna:str):
    if rna.count("A") == rna.count("U") and rna.count("C") == rna.count("G"):
        return True

matches = [("A","U"), ("U","A"), ("C","G"), ("G","C")]

def cat(seq, memo = {}):
    n = len(seq) // 2
    if n <= 1:
        return 1
    if seq in memo:
        return memo[seq]
    
    catalan_count = 0
    for m in range(1, 2*n, 2):
        r_seq = seq[1:m]
        l_seq = seq[m+1:]
        if (seq[0], seq[m]) in matches and valid_seq(r_seq):
            catalan_count += cat(r_seq, memo) * cat(l_seq, memo)
    memo[seq] = catalan_count%1000000
    return catalan_count%1000000

print(cat(seq))