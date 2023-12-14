"""Given a DNA sequence, return the transcription into RNA:"""

f = open("datasets/rosalind_rna.txt", "r")
dna = f.read()

rna = dna.replace("T", "U")
print(rna)