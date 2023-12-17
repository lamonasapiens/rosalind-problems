"""Given: Six nonnegative integers, each of which does not exceed 20000
The integers correspond to the number of couples in a population
possessing each genotype pairing for a given factor. In order, the six
given integers represent the number of couples having the following
genotypes:

g1 = AA-AA
g2 = AA-Aa
g3 = AA-aa
g4 = Aa-Aa
g5 = Aa-aa
g6 = aa-aa

Return: The expected number of offspring displaying the dominant
phenotype in the next generation, under the assumption that every
couple has exactly two offspring.
_____________________________________________________________________
"""

f = open("datasets/rosalind_iev.txt", "r")
g1, g2, g3, g4, g5, g6 = (int(x) for x in f.read().split())

offspring = 2
PA_g1 = 1*offspring*g1
PA_g2 = 1*offspring*g2
PA_g3 = 1*offspring*g3
PA_g4 = 0.75*offspring*g4
PA_g5 = 0.5*offspring*g5
PA_g6 = 0*offspring*g6

dominant_offspring = PA_g1 + PA_g2 + PA_g3 + PA_g4 + PA_g5 + PA_g6

print(dominant_offspring)