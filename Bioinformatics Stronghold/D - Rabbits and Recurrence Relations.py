"""Calculate the total number of rabbit pairs that will be present
after n months, if we begin with 1 pair and in each generation, every
pair of reproduction-age rabbits produces a litter of k rabbit pairs
(instead of only 1 pair)."""

f = open("datasets/rosalind_fib.txt", "r")
n, k = f.readline().strip().split(" ")


def F(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1, k) + k*F(n-2, k)

print (F(n, k))