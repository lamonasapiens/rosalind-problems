"""Calculate the Hamming distance (i.e. nº of point mutations) between
two DNA sequences:"""

def clean_fasta(fasta):
    """given a str with 2 DNAs, returns one list for each DNA"""
    sequences = fasta.split()
    seq1 = sequences[0]
    seq2 = sequences[1]
    return seq1, seq2

def mutations(seq1, seq2):
    """given 2 strings, it counts the nº of differences between them
    (=Hamming distance)"""
    return sum(i != j for i, j in zip(seq1, seq2))

    
f = open("datasets/rosalind_hamm.txt", "r")
FASTA = f.read()

seq1, seq2 = clean_fasta(FASTA)
print(mutations(seq1, seq2))