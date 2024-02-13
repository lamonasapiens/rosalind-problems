"""
Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s
of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s
are constructed with GC-content x (see “Introduction to Random Strings”), then at
least one of the strings equals s. We allow for the same random string to be created
more than once.
______________________________
Comment:
The given GC-content definition is not precise in this problem. x represents the 
probability that one G or C occurs in any position of a random string.
____________________________________________________________________________________
"""

import random
f = open("datasets/sample.txt", "r")
values, dna = f.read().strip().split("\n", 1)

dna = dna.replace("\n","")
N, x = values.split()
N = int(N)
x = float(x)

freqs = {
    "G" : x/2,
    "C" : x/2,
    "A" : (1-x)/2,
    "T" : (1-x)/2,
    }

P = 1
for i in dna:
    P *= freqs[i]

notP = 1-P

result = 1-(notP**N)
print(result)
