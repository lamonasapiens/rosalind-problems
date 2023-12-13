f = open("datasets/rosalind_dna.txt", "r")
sample = f.read()

def count2(DNA):
    A = DNA.count("A")
    C = DNA.count("C")
    G = DNA.count("G")
    T = DNA.count("T")
    return A, C, G, T

a2, c2, g2, t2 = count2(sample)
print(f"{a2} {c2} {g2} {t2}")
