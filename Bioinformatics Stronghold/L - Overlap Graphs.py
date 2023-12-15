"""For a collection of strings and a positive integer k, the overlap
graph for the strings is a directed graph "Ok" in which each string is
represented by a node, and string s is connected to string t with a
directed edge when there is a length k suffix of s that matches a
length k prefix of t, as long as s≠t; we demand s≠t to prevent
directed loops in the overlap graph (although directed cycles may be
present)

Given a collection of DNA strings in FASTA format, return the
adjacency list corresponding to "O3"."""


f = open("datasets/rosalind_grph.txt", "r")
FASTA = f.read()

def clean_fasta(fasta: str):
    """Given a string in FASTA format, returns a dictionary with the
    IDs as keys and DNAs as values"""
    sequences = fasta.split(">")[1:]
    dictionary = {}
    for i in sequences:
        lines = i.split("\n", 1)
        ID = lines[0]
        dna = lines[1].replace("\n", "")
        dictionary[ID] = dna
    return dictionary


def graph(sequences: dict):
    """Given a dictionary with IDs and dna sequences, returns the adjacency list corresponding to O3"""
    adjacency = ""
    for key1, seq1 in sequences.items():
        prefix = seq1[-3:]
        for key2, seq2 in sequences.items():
            if seq2.startswith(prefix) and key1 != key2:
                adjacency += f"{key1} {key2}\n"
    return adjacency


DNAs = clean_fasta(FASTA)
print(graph(DNAs))