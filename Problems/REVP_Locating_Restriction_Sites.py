"""A DNA string is a reverse palindrome if it is equal to its reverse
complement. For instance, GCATGC is a reverse palindrome because its
reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the
string having length between 4 and 12. You may return these pairs in
any order.
_____________________________________________________________________
"""
f = open("datasets/rosalind_revp.txt", "r")
DNA = f.read().split("\n", 1)[1].replace("\n", "")

def complement(dna:str):
    Cdna = dna.lower()[::-1]\
        .replace("a", "T")\
            .replace("t", "A")\
                .replace("c", "G")\
                    .replace("g", "C")
    return Cdna


"""Here we create a list with the possition and length of all the
possible palindromes of 4-12bp"""
palindromes = []
length = len(DNA)

for i in range(length-3):
    for j in range(4, 13):
        if i+j > length:
            break
        else:
            seq = DNA[i:i+j]
            if seq == complement(seq):
                palindromes.append([i+1, len(seq)])       

for pal in sorted(palindromes):
    print(*pal)