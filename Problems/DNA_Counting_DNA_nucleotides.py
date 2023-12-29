"""Count the number of each nucleotide on a DNA sequence:"""

f = open("datasets/rosalind_dna.txt", "r")
sample = f.read()

def count(DNA):
    A = DNA.count("A")
    C = DNA.count("C")
    G = DNA.count("G")
    T = DNA.count("T")
    return A, C, G, T

a, c, g, t = count(sample)
print(a, c, g, t)