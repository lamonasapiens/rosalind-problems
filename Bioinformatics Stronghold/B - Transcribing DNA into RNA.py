f = open("datasets/rosalind_rna.txt", "r")
dna = f.read()


rna = dna.replace("T", "U")
print(rna)
