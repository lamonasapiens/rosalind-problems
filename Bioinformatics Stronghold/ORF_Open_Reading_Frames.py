"""
An open reading frame (ORF) is one which starts from the start codon
and ends by stop codon, without any other stop codons in between.
Thus, a candidate protein string is derived by translating an open
reading frame into amino acids until a stop codon is reached.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated.
Strings can be returned in any order.
______________________________________________________________________
"""
import re

aminoacids = {
    "UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L",
    "CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L",
    "AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M",
    "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V",
    "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S",
    "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
    "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
    "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
    "UAU" : "Y", "UAC" : "Y", "UAA" : " ", "UAG" : " ",
    "CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q",
    "AAU" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K",
    "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", 
    "UGU" : "C", "UGC" : "C", "UGA" : " ", "UGG" : "W",
    "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R",
    "AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R",
    "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G",
}

f = open("datasets/rosalind_orf.txt", "r")
DNA = f.read().split("\n", 1)[1].replace("\n", "")


#Convert DNA to RNA
RNA = DNA.replace("T", "U")

#Complementary RNA
inverted_rna = RNA.lower()[::-1]
cRNA = inverted_rna\
    .replace("a", "U")\
        .replace("u", "A")\
            .replace("c", "G")\
                .replace("g", "C")


#Translate the RNA sequences into aminoacids:
def translation(rna):
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        protein += aminoacids[codon]
    return protein


#Define the ORF sequence
ORF = re.compile(r"M.*? ")


#Search for the possible proteins:
proteins = set()
for i in range(0,3):
    seq1, seq2 = translation(RNA[i:]), translation(cRNA[i:])
    for seq in seq1, seq2:
        for j in range(len(seq)):
            prot = re.search(ORF,seq[j:])
            if prot != None:
                proteins.add(prot.group())
    
    
print("\n".join(i for i in list(proteins)))