"""A partial permutation is an ordering of only k objects taken from a collection
containing n objects (i.e., k≤n). For example, one partial permutation of three 
of the first eight positive integers is given by (5,7,2).

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
________________________________________________________________________________
"""

f = open("datasets/rosalind_pper.txt", "r")
n, k = f.read().strip().split()
n = int(n)
k = int(k)

result = 1
for i in range(k):
    result = (result * (n - i)) % 1000000
print(result)

"""This loop calculates directly the number of partial permutations, knowing
that P(n,k) = n! / (n-k)! which is the same as n*(n-1)*(n-2)...(n-k+1)"""