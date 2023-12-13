
def complement(dna):
    inverted_dna = dna.lower()[::-1]
    Cdna = inverted_dna\
        .replace("a", "T")\
            .replace("t", "A")\
                .replace("c", "G")\
                    .replace("g", "C")
    return Cdna


s = input("your DNA: ")
print(complement(s))