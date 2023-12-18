"""Given a collection of UniProt Protein Database access IDs.
For each protein possessing the N-glycosylation motif, return its ID
followed by a list of locations in the protein string where the
motif can be found.

The N-glycosylation motif is represented as follows: N{P}[ST]{P}
where {P} = "any aminoacid but P"
and [ST] = "S or T"
_____________________________________________________________________
"""
import requests
import re

f = open("datasets/rosalind_mprt.txt", "r")
IDs = f.read().split()

URL = "https://rest.uniprot.org/uniprotkb/<id>.fasta"



#Fetch the data from the URL for each ID and store it in a dictionary:
FASTA = {}
for id in IDs:
    newURL = URL.replace("<id>", id[:6])
    response = requests.get(newURL)

    if response.status_code == 200:
        FASTA[id] = response.text.split("\n",1)[1].replace("\n", "")


N_glyc = r"N[^P][ST][^P]"

#Search for the N_glyc motif on each sequence and return the positions
positions = {}
for key, seq in FASTA.items():
    positions[key] = []
    for i in range(len(seq)):
        if re.match(N_glyc, seq[i:i+4]):
            positions[key].append(i+1)
    if positions[key] == []:
        del positions[key]
    
    
for key, value in positions.items():
     print(key)
     print(*value)