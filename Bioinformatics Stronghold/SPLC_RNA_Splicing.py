"""Given: A DNA string (s) and a collection of substrings of s
acting as introns. Return: A protein string resulting from 
transcribing and translating the exons of s. 

(Note: Only one solution will exist for the dataset provided.)
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

f = open("datasets/rosalind_splc.txt", "r")
sequences = f.read().split(">")[1:]

DNA = sequences[0].split("\n", 1)[1].replace("\n", "")
introns = [i.split("\n", 1)[1].replace("\n", "") for i in sequences][1:]


#Remove the introns from the DNA
for intron in introns:
    DNA = DNA.replace(intron, "")

#DNA to RNA transcription
mRNA = DNA.replace("T", "U")

#RNAm to protein translation
protein = ""
for i in range(0, len(mRNA)-2, 3):
    codon = mRNA[i:i+3]
    if aminoacids[codon] == " ":
        break
    else:
        protein += aminoacids[codon]
    
print(protein)