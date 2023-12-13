f = open("datasets/rosalind_iprb.txt", "r")
k, m, n = [int(x) for x in f.readline().split()]

total = k + m + n

total_alelos = 2 * total
alelo_A = 2*k + m
alelo_a = 2*n + m

Pr_kk = (k/total) * ((k-1)/(total-1))
Pr_km = 2 * ((k/total) * (m/(total-1)))
Pr_kn = 2 * ((k/total) * (n/(total-1)))
Pr_mm = (m/total) * ((m-1)/(total-1))
Pr_mn = 2* ((m/total) * (n/(total-1)))
Pr_nn = (n/total) * ((n-1)/(total-1))

Pr_alelo_A = Pr_kk + Pr_km + Pr_kn + Pr_mm*(3/4) + Pr_mn*(2/4)

print(Pr_alelo_A)






