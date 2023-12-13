
f = open("datasets/rosalind_gc.txt", "r")
FASTA = f.read()


def clean_fasta(fasta: str):
    """Given a string in FASTA format, returns a dictionary with the IDs as keys and DNAs as values"""
    sequences = fasta.split(">")[1:]
    dictionary = {}
    for i in sequences:
        lines = i.split("\n", 1)
        ID = lines[0]
        dna = lines[1].replace("\n", "")
        dictionary[ID] = dna

    return dictionary


def gc_content(fasta_dictionary: dict):
    """Given a dictionary of DNA sequences, returns another dictionary with the GC percentage of each sequence"""
    for key, value in fasta_dictionary.items():    
        fasta_dictionary[key] = ((value.count("C") + value.count("G")) / len(value))*100
    return fasta_dictionary


result = gc_content(clean_fasta(FASTA))

"""Calculate the sequence with highest GC content:"""
max_key = max(result, key = lambda k: result[k])
max_value = result[max_key]
print(max_key)
print(max_value)
