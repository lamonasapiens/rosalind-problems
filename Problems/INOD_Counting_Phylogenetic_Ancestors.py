"""
Given: A positive integer n(3≤n≤10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.
_________________________________________________________________________________
"""
f = open("datasets/rosalind_inod.txt", "r")
n = int(f.read().strip())

nodes = n-2
print(nodes)