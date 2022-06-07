# prim-algorithm
Python implementation of Prim's algorithm. Takes a graph and calculates a minimum spanning tree.

The graph has to fulfill the following requirements for the algorithm to work
- The graph is fully connected and unidirectional
- The edges are weighted

The graph is presented in a list of edges, which consists of tuples whose first two entries are the two vertices and the third is the weight of the edge.

Example:
[(0,1,4), (1,6,3)]
Being a graph of the vertices 0, 1 and 6 and an edge between 0 and 1 with a weight of 4 and an edge between 1 and 6 with the weight of 3.
The minimum spanning tree is returned in the exact same layout.
