"""Recall the definition of the Fibonacci numbers from “Rabbits and
Recurrence Relations”, which followed the recurrence relation Fn=Fn−
+Fn−2 and assumed that each pair of rabbits reaches maturity in one
month and produces a single pair of offspring (one male, one female
each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a
dynamic programming solution in the case that all rabbits die out
after a fixed number of months (m) """


f = open("datasets/rosalind_fib.txt", "r")
n, k = f.readline().strip().split(" ")


def F(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1, k) + k*F(n-2, k)

print (F(n, k))