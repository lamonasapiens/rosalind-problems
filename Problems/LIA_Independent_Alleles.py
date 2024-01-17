"""Given: Two positive integers k and N. In this problem, we begin with Tom,
who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st
generation, each of whom has two children, and so on. Each organism always
mates with an organism having genotype Aa Bb.

Return: The probability that at least N AaBb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.
_______________________________________________________________________________
"""
from math import factorial

f = open("datasets/rosalind_lia.txt")
k, n = f.read().strip().split()
k = int(k)
n = int(n)

def combinations(y, x):
    return (factorial(y))/(factorial(x) * factorial(y-x))

P_not_AaBb = 3/4
P_AaBb = 1/4
kids = 2**k


def binomial(y, x):
    result = 0
    for i in range(x, kids+1):
        result += combinations(y,i) * (P_AaBb**i) * (P_not_AaBb**(y-i))
    return result

print(binomial(kids,n))

"""
EXPLANATION:

The probability of having a kid with AaBb genotype is always 1/4 for every
couple (1/2 Aa * 1/2 Bb). Therefore, P_not_AaBb is the probability of NOT having
a AaBb kid (=3/4).

The problem is solved using the formula of Binomial Distribution, which calculates the
probability of having EXACTLY x successess in y trials: 

P(x = 2) = (y,x) * p^x * (1-p)^(y-x)

where:
    p   = probability of success    (= 1/4 in our case)
    1-p = probability of failure    (= 3/4 in our case)
    y   = total nº of trials        (= 2^k in our case, the nº of kids)
    x   = total nº of successes     (= n in our case, the nº of kids with AaBb)
    (y,x) = nº of combinations to get x successes in y trials = [y! / x!(y-x)!]

The probability of having AT LEAST n successes, is calculated using a for loop that adds
the probabilities for each possible n.
"""
