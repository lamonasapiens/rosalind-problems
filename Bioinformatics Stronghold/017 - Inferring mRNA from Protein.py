"""Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the
protein could have been translated, modulo 1,000,000. (Don't neglect
the importance of the stop codon in protein translation.)
__________________________________________________________________
"""


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

f = open("datasets/rosalind_mrna.txt", "r")
protein = f.readline().strip()

def rev_translation(prot):
    total = 3
    for aa in prot:
        total *= (sum(1 if i == aa else 0 for i in aminoacids.values()))
    return total % 1000000

print(rev_translation(protein))



"""________________________________________________________________
The solution is simpler if we use a dictionary with the codons
as keys and the aminoacids as values:

codons = {'F': ['UUU', 'UUC'],
            'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
            'Y': ['UAU', 'UAC'],
            '*': ['UAA', 'UAG', 'UGA'],
            'C': ['UGU', 'UGC'],
            'W': ['UGG'],
            'P': ['CCU', 'CCC', 'CCA', 'CCG'],
            'H': ['CAU', 'CAC'],
            'Q': ['CAA', 'CAG'],
            'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'V': ['GUU', 'GUC', 'GUA', 'GUG'],
            'A': ['GCU', 'GCC', 'GCA', 'GCG'],
            'D': ['GAU', 'GAC'],
            'E': ['GAA', 'GAG'],
            'G': ['GGU', 'GGC', 'GGA', 'GGG'],
            'I': ['AUU', 'AUC', 'AUA'],
            'M': ['AUG'],
            'T': ['ACU', 'ACC', 'ACA', 'ACG'],
            'N': ['AAU', 'AAC'],
            'K': ['AAA', 'AAG']}


In that case, the function rev_translation would be as follows:

def rev_translation(prot):
    total = 3
    for aa in prot:
        total *= len(codons[aa])
    return total % 1000000
"""
