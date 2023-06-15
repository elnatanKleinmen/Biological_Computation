# Biological_Computation
PART 1

a) We wrote a program (in python) that gets as input a positive integer 𝑛 and generates all connected sub-graphs of size 𝑛.
The output is a textual file of the following form:
    n=2 count=2
    #1
    1 2
    #2
    1 2
    2 1
The first two lines output n and the total number (count) of different sub-graphs of size n.
Then the sub-graphs themselves are given each starting with a line labelled #k for motif number followed by all edges,
each line i j means an edge from source i to target j.

b) **The main program generates all connected sub-graphs of size 𝑛 for n in range 0 to 4 and save the results in the file "all_sub_graphs_of_size_n".**


PART 2
We wrote a program that gets as input positive integer 𝑛 and a graph of the format:
    1 2
    2 3
    1 4
The graph in the example contains 4 vertices 1,2,3,4 and directed edges (1,2) (2,3) (1,4).
**The program outputs all sub-graphs of size 𝑛 and count how many instances appear of each motif. to the file "all_sub_graphs_of_size_n_counting".**
The format of the output of the identified sub-graphs is like in part 1,
where in the line after #k should appear the count of number of instances, 
count=m if the motif appears m times. 
Output count=0 if a motif does not appear in the graph.

In the main program you can choose one of this options:

  Enter 1 and the program compute the results to the graph:
          1 2
          2 3
          1 3
          3 4
        
  Enter 2 and than the edges of the graph, as ints, first the source vertex of the egde and then the destination vertex of the egde. 
  
**The program outputs all sub-graphs of size 𝑛 and the count of  how many instances appear of each motif to the file "all_sub_graphs_of_size_n_counting"
for the chosen graph and n in range 0 to 4.**
