"""Given: A permutation of at most 12 symbols defining an ordered alphabet A
and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. 
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on 
the order in which the symbols are given.)
______________________________________________________________________________________
"""

from itertools import product

f = open("datasets/rosalind_lexv.txt", "r")
symbols, n = f.readlines()
symbols = [i for i in symbols.replace(" ","").strip()]
n = int(n)

#Create a custom dictionary that stores the order of the symbols:
dictionary = {value:key for key, value in enumerate(symbols)}

#Generate all the possible combinations between the symbols, of length 1:n
words = []
for i in range(1,n+1):
    for symbol in product(symbols, repeat = i):
        words.append("".join(symbol))

#Define a custom function for sorting that uses first the order of the characters
#in the dictionary, and then the length of the word.
def sorting(word):
    return ([dictionary[char] for char in word], len(word))

#Sort the list of the words
sorted_words = sorted(words, key = sorting)
print(*sorted_words)