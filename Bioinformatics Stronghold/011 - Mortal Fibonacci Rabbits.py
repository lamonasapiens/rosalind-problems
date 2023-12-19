"""Recall the definition of the Fibonacci numbers from “Rabbits and
Recurrence Relations”, which followed the recurrence relation Fn=Fn−
+Fn−2 and assumed that each pair of rabbits reaches maturity in one
month and produces a single pair of offspring (one male, one female
each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a
dynamic programming solution in the case that all rabbits die out
after a fixed number of months (m) """


f = open("datasets/rosalind_fibd.txt", "r")
n, m = f.readline().strip().split(" ")


#This function uses dynamic programming to improve performance
def F(n, m, memo={}):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    if n <= m:
        result = F(n-1, m, memo) + F(n-2, m, memo)
    else:
        result = sum(F(n-i, m, memo) for i in range(2,m+1))
    memo[(n, m)] = result
    return result
    

print(F(int(n),int(m)))