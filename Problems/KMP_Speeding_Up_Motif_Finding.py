"""
A prefix of a length n string s is a substring s[1:j]; a suffix of s
is a substring s[k:n]. The failure array of s is an array P of length n
for which P[k] is the length of the longest substring s[j:k] that is equal 
to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would
always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
____________________________________________________________________________
"""

f = open("datasets/rosalind_kmp.txt", "r")
s = f.read().strip().split("\n",1)[1].replace("\n","")

n = len(s)
P = [0]*n #Here, P is equivalent to the lps[] matrix in the KMP algorythm. That is, "the longest proper prefix which is also a suffix"


m = 0 #this variable keeps track of the length of the longest prefix sufix value
k = 1
while k <= n-1:
    if s[m] == s[k]:
        m += 1
        P[k] = m
        k += 1
    else:
        if m != 0:
            m = P[m-1]
        else:
            P[k] = 0
            k += 1

print(*P)