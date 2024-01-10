"""
Given: At most 50 DNA strings of approximately equal length in FASTA format
(which represent reads deriving from the same strand of a single linear
chromosome).

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome). The dataset is guaranteed to
satisfy the following condition: there exists a unique way to reconstruct the
entire chromosome from these reads by gluing together pairs of reads that
overlap by more than half their length.
"""

f = open("datasets/rosalind_long.txt")
FASTA = f.read().strip().split(">")[1:]
sequences = []

for id in FASTA:
    lines = id.split("\n", 1)[1].replace("\n", "")
    sequences.append(lines)

def prefix(seq1, seq2):
    length = min(len(seq1), len(seq2))
    motif_len = int((length/2)-1)
    motif = ""
    for i in range(motif_len, length+1):
        if seq1[-i:] == seq2[:i]:
            motif += seq2[i:] 
    return motif


#Search for the first sub-sequence of the chromosome (his prefix should not overlap with the rest of the sequences). Once found, we remove the seq from the list and repete the process.
chromosome = ""
x = len(sequences)
while x > 0:
    for i in sequences:
        count = 0
        for j in sequences:
            if prefix(j,i) == "":
                count += 1 
        if count == len(sequences):
            if chromosome == "":
                chromosome += i
            else:
                chromosome += prefix(chromosome, i)
            sequences.remove(i)
            x -= 1
            break

print(chromosome)