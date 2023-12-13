f = open("datasets/rosalind_fib.txt", "r")
n, k = f.readline().strip().split(" ")


def F(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1, k) + k*F(n-2, k)

print (F(n, k))