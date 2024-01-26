"""Given: A collection of up to 1000 reads of equal length (at most 50 bp)
in FASTA format. Some of these reads were generated with a single-nucleotide 
error. For each read s in the dataset, one of the following applies:

--- s was correctly sequenced and appears in the dataset at least twice 
(possibly as a reverse complement);
--- s is incorrect, it appears in the dataset exactly once, and its Hamming 
distance is 1 with respect to exactly one correct read in the dataset (or its
reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]".
(Each correction must be a single symbol substitution, and you may return 
the corrections in any order.)
______________________________________________________________________________
"""

f = open("datasets/rosalind_corr.txt","r")
seqs = [seq.replace("\n","") for seq in f.readlines()[1::2]]

def rev_comp(seq:str):
    """Gives the reversed complementary seq of DNA: ATT -> AAT"""
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def mutations(seq1, seq2):
    """given 2 strings, it counts the nº of differences between them
    (=Hamming distance)"""
    return sum(i != j for i, j in zip(seq1, seq2))

correct = set()
mutated = set()
rc_seqs = [rev_comp(seq) for seq in seqs]

for seq in seqs:
    if seq in rc_seqs or seqs.count(seq)>1:
        correct.add(seq)
        correct.add(rev_comp(seq))
    else:
        mutated.add(seq)

for seq1 in mutated:
    for seq2 in correct:
        if mutations(seq1,seq2) == 1:
            print(f"{seq1}->{seq2}")