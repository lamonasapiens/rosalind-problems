f = open("datasets/rosalind_subs.txt", "r")

DNA, motif = f.read().split()


def pos_motifs(dna, motif):
    """Given a DNA sequence and a repetitive motif, returns a list with the positions of the motif on the DNA"""
    positions = []
    for i in range(len(dna)-len(motif)+1):
        if dna[i:i+len(motif)] == motif:     
            positions.append(i+1)
    return positions

print(*pos_motifs(DNA, motif))


