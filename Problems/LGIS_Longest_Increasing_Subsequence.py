"""
Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing
subsequence of π.

A subsequence is increasing if the elements of the subsequence increase, and
decreasing if the elements decrease. For example, given the permutation (8, 2
1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a
decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two
subsequences are as long as possible.
________________________________________________________________________________
"""
f = open("datasets/rosalind_lgis.txt", "r")
n, seq = f.read().strip().split("\n")
n = int(n)
seq = [int(x) for x in seq.split()]


def find_max_sequence(seq):
    n = len(seq)

    # Initialize lists to store lengths of ascending and descending sequences
    asc_lengths = [1] * n
    desc_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Update ascending sequence length
            if seq[i] > seq[j] and asc_lengths[i] < asc_lengths[j] + 1:
                asc_lengths[i] = asc_lengths[j] + 1

            # Update descending sequence length
            if seq[i] < seq[j] and desc_lengths[i] < desc_lengths[j] + 1:
                desc_lengths[i] = desc_lengths[j] + 1

    # Find the maximum length and corresponding sequence for ascending and descending
    max_asc_length = max(asc_lengths)
    max_desc_length = max(desc_lengths)

    asc_seq = []
    desc_seq = []

    # Find the ascending sequence
    for i in range(n - 1, -1, -1):
        if asc_lengths[i] == max_asc_length:
            asc_seq.append(seq[i])
            max_asc_length -= 1

    # Find the descending sequence
    for i in range(n - 1, -1, -1):
        if desc_lengths[i] == max_desc_length:
            desc_seq.append(seq[i])
            max_desc_length -= 1

    return asc_seq[::-1], desc_seq[::-1]

asc_seq, desc_seq = find_max_sequence(seq)

print(*asc_seq)
print(*desc_seq)