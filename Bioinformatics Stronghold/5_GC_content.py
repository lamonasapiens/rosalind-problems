
f = open("rosalind_gc.txt", "r")
FASTA = f.read()


def clean_fasta(fasta):
    sequences = fasta.split(">")[1:]
    dictionary = {}
    for i in sequences:
        lines = i.split("\n", 1)
        ID = lines[0]
        dna = lines[1].replace("\n", "")
        dictionary[ID] = dna

    return dictionary

def gc_content(fasta_dictionary):
    for key, value in fasta_dictionary.items():    
        fasta_dictionary[key] = ((value.count("C") + value.count("G")) / len(value))*100
    return fasta_dictionary


result = gc_content(clean_fasta(FASTA))
max_key = max(result, key = lambda k: result[k])
max_value = result[max_key]
print(max_key)
print(max_value)
