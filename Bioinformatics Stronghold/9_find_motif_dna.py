f = open("dna_motif.txt", "r")

DNA = f.read()
motif = "CGACATGCG"



def pos_motifs(dna, motif):
    """Given a DNA and a motif, returns the positions of the repetitive motive on the DNA string"""
    positions = []
    for i in range(len(dna)-len(motif)+1):
        if dna[i:i+len(motif)] == motif:     
            positions.append(i+1)
    return positions

print(pos_motifs(DNA, motif))


