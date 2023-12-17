"""Given: A collection of k(k≤100) DNA strings of length at most 1kbp
each in FASTA format. Return: The longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
____________________________________________________________________
"""

def clean_fasta(fasta: str):
    """It cleans the FASTA and returns a list of DNA strings, without the ID"""
    sequences = fasta.split(">")[1:]
    return [i.split("\n", 1)[1].replace("\n", "") for i in sequences]


def longest_motif(dnas: list):
    """Given a collection of DNAs on a list, this function finds the longest common subsequence among them"""
  
    shortest_seq = min(dnas, key = lambda x: len(x))
    all_motifs = set()
    motif = ""

    #Add all the possible motifs to the set:
    for i in range(len(shortest_seq)+1):
        for j in range(i+1, len(shortest_seq)+1):
            all_motifs.add(shortest_seq[i:j])
    
    #Look for the longest motif on the set that exists in all the sequences
    motif += max(all_motifs, key = lambda x: len(x) if all(x in dnas[seq] for seq in range(len(dnas))) else 0)
    
    return motif


f = open("datasets/rosalind_lcsm.txt", "r")
FASTA = f.read()

result = longest_motif(clean_fasta(FASTA))
print(result)