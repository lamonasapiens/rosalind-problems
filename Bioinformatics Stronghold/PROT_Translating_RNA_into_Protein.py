"""Return the protein string encoded by a given DNA sequence:"""

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


def translation(rna):
    """Returns the sequence of aminoacids translated from a RNA 
    sequence"""
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        protein = protein + aminoacids[codon]
    return protein


f = open("datasets/rosalind_prot.txt", "r")
RNA = f.read()

print(translation(RNA))