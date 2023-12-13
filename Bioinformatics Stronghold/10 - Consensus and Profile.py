f = open("datasets/rosalind_cons.txt", "r")
FASTA = f.read()

def clean_fasta(fasta: str):
    """It cleans the FASTA and returns a list of DNA strings, without the ID"""
    sequences = fasta.split(">")[1:]
    lista = []
    for i in sequences:
        line = i.split("\n", 1)[1]
        lista.append(line.replace("\n", ""))
    return lista


def profile(DNAs):
    """Given a list with DNA strings of equal length, it returns: A "profile dictionary" where keys = nucleotides : values = list of the frequencies for that nucleotide on each position"""
    profile_dict = {
        "A" : [0]*len(DNAs[0]),
        "C" : [0]*len(DNAs[0]),
        "G" : [0]*len(DNAs[0]),
        "T" : [0]*len(DNAs[0])
    }
    for i in DNAs:
        for index, j in enumerate(i):
            profile_dict[j][index] += 1
    return profile_dict


def consensus(prof:dict):
    """Given a "profile dictionary", returns a string representing the consensus DNA"""
    highest = []
    result = ""
    for i in zip(*prof.values()):
        highest.append(max(i))
    for index in range(len(highest)):
        for key in prof.keys():
            if highest[index] == prof[key][index]:
                result += key
                break
    return result
        


DNAs = clean_fasta(FASTA)
profile_matrix = profile(DNAs)
consensus_string = consensus(profile_matrix)

print(consensus_string)

for i, j in profile_matrix.items():
    print(f"{str(i)}:", str(j).replace(",", "").replace("[", "").replace("]", ""))


