"""Given: A positive integer n (n≤1000) and an adjacency list corresponding
to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
______________________________________________________________________________________
"""
f = open("datasets/rosalind_tree.txt", "r")
lines = f.read().strip().split("\n")

nodes = int(lines[0])
lines.pop(0)
adj_list = lines

"""A connected tree of n nodes will always contain n-1 edges. So, the formula to 
calculate the minimum nº of edges without cycles is:
total nº of nodes - nº of provided edges - 1
"""
total_edges = len(adj_list)
min_edges = nodes - total_edges - 1
print(min_edges)