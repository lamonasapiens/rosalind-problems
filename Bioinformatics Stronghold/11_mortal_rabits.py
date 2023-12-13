"""def F(n, m):
    rabbits = [0] * (n+2)
    
    rabbits[1] = 1
    rabbits[2] = 1

    for i in rabbits:
        while m >= 2:
            rabbits[i] = rabbits[i-m]
            m -=1
    return rabbits[n]
"""



def F(n, k):
    total = 0
    if n == 1 or n == 2:
        return 1
    else:
        sum(F(n-(i-1), k)) for i in range(2,k)

    return total

print (F(1,3))
print (F(2,3))
print (F(3,3))
print (F(4,3))
print (F(5,3))
print (F(6,3))
print (F(7,3))
print (F(8,3))
print (F(9,3))
print (F(10,3))





