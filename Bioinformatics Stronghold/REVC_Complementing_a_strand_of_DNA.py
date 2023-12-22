"""Given a DNA sequence, return the complementary string:"""

def complement(dna):
    inverted_dna = dna.lower()[::-1]
    Cdna = inverted_dna\
        .replace("a", "T")\
            .replace("t", "A")\
                .replace("c", "G")\
                    .replace("g", "C")
    return Cdna


f = open("datasets/rosalind_revc.txt", "r")
DNA = f.read()

print(complement(DNA))