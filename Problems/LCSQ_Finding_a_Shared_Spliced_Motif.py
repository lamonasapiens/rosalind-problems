"""
A string u is a common subsequence of strings s and t if the symbols of u
appear in order as a subsequence of both s and t. For example, "ACTG" is a 
common subsequence of "AACCTTGG" and "ACACTGTGA".

Analogously to the definition of longest common substring, u is a longest 
common subsequence of s and t if there does not exist a longer common 
subsequence of the two strings. Continuing our above example, "ACCTTG" is a
longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, 
you may return any one.)
__________________________________________________________________________________
"""

f = open("datasets/rosalind_lcsq.txt", "r")
seqs = f.read().strip().split(">")[1:]

s = seqs[0].split("\n",1)[1].replace("\n", "")
t = seqs[1].split("\n",1)[1].replace("\n", "")

lenS = len(s)
lenT = len(t)


"""STEP 1: initialize the matrix of (s+1)x(t+1). We ad one extra row and column
to accomodate for the base cases and to handle the cases of empty strings:"""
matrix = [[0] * (lenT+1) for _ in range(lenS + 1)]


"""STEP 2: build the matrix using dynamic programming:"""
for i in range(1, lenS+1):
    for j in range(1, lenT+1):
        """if the current character of s and t match, then we can extend the LCS
        (Longest Common Substring) by incrementing the value of matrix[i][j] by 1
         compared to the previous characters"""
        if s[i-1] == t[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])


"""STEP 3: reconstruct the longest common subseq from the matrix (LCS):
We start from the bottom-right corner of the matrix. When the characters match, 
we add that character to the LCS and move diagonally towards matrix[0][0]. If the
characters don´t match, we move towards the maximun value (up or left):"""
LCS = []
i, j = lenS, lenT
while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        LCS.append(s[i-1])
        i -= 1
        j -= 1
    elif matrix[i - 1][j] > matrix[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(LCS[::-1]))