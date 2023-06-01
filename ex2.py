import copy
import time
from datetime import datetime


def remove_not_connected_graphs(graphs):
    connected_graphs = []
    for graph in copy.deepcopy(graphs):
        undirected_graph = undirect_graph(graph)
        if not graph or is_connected(undirected_graph):
            connected_graphs.append(graph)
    return connected_graphs


global visited


def is_connected(graph):
    # Initialize a set to keep track of visited vertices
    global visited
    visited = set()

    # Choose any vertex in the graph
    start_vertex = next(iter(graph.keys()))

    # Call DFS starting from the chosen vertex
    dfs(start_vertex, graph)

    return len(visited) == len(graph)


def undirect_graph(graph):
    undirected_graph = copy.deepcopy(graph)
    for key in graph:
        if graph.get(key, []):
            for v in graph[key]:
                if key not in undirected_graph.get(v, []):
                    undirected_graph[v] = undirected_graph.get(v, []) + [key]
    return undirected_graph


def dfs(vertex, graph):
    global visited
    # Mark the current vertex as visited
    visited.add(vertex)
    #print(visited)

    # Visit all vertices that are directly connected to the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, graph)


def remove_isomorphic_graphs(graphs):
    isomorphic_graphs = []
    for new_graph in graphs:
        find_isomorphic = False
        for graph in isomorphic_graphs:
            if is_isomorphic(new_graph, graph):
                find_isomorphic = True
                break
        if not find_isomorphic:
            isomorphic_graphs.append(new_graph)
    return isomorphic_graphs


def is_isomorphic(g1, g2):
    _g1, _g2 = graph_ordering(g1), graph_ordering(g2)
    all_isomorphic = get_all_isomorphic(_g1)

    for g3 in all_isomorphic:
        if is_equal_graphs(_g2, g3):
            return True
    return False


def graph_ordering(g):
    if max(g) == len(g):
        return g
    new_nodes = [v for v in range(1, max(g)+1) if v not in g and v <= len(g)]  # v_not_in_g
    old_nodes = [v for v in g if v > len(g)]  # v_over_len

    switched_graph = g.copy()
    for old_node, new_node in zip(old_nodes, new_nodes):
        if old_node in switched_graph:
            neighbors = switched_graph.pop(old_node)
            switched_graph[new_node] = neighbors
            for node, node_neighbors in switched_graph.items():
                if old_node in node_neighbors:
                    node_neighbors.remove(old_node)
                    node_neighbors.append(new_node)

    return switched_graph


def get_all_isomorphic(g):
    all_isomorphic = []
    permutations = get_permutations(len(g))
    for permutation in permutations:
        all_isomorphic.append(switch_vertices(g, permutation))
    return all_isomorphic


def switch_vertices(graph, permutation):
    switched_graph = {}

    # Iterate over each vertex in the original graph
    for vertex, neighbors in graph.items():
        # Compute the switched vertex based on the permutation
        switched_vertex = permutation[vertex - 1]  # Adjust index to match permutation

        # Compute the switched neighbors by adjusting the indices of the neighbors
        switched_neighbors = [permutation[n - 1] for n in neighbors]

        # Add the switched vertex and switched neighbors to the switched graph
        switched_graph[switched_vertex] = switched_neighbors

    return switched_graph


def get_permutations(n):
    numbers = list(range(1, n + 1))
    permutations = []
    generate_permutations(numbers, 0, n - 1, permutations)
    return permutations


def generate_permutations(numbers, left, right, permutations):
    if left == right:
        permutations.append(numbers[:])
    else:
        for i in range(left, right + 1):
            numbers[left], numbers[i] = numbers[i], numbers[left]
            generate_permutations(numbers, left + 1, right, permutations)
            numbers[left], numbers[i] = numbers[i], numbers[left]


def is_equal_graphs(g1, g2):
    # Check if the dictionaries have the same keys
    if set(g1.keys()) != set(g2.keys()):
        return False

    # Check if the values for each key are equal
    for key in g1:
        # Check if the lists have the same elements
        if set(g1[key]) != set(g2[key]):
            return False

    # If all checks pass, the dictionaries are equal
    return True


def get_all_connected_graphs_with_print(n):
    # input: int n
    # output: all connected graphs with n vertices
    if not n:
        return []

    print(f"\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% {n=} %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    print(f"\n--------------------sub_graphs------------------------")
    sub_graphs = get_all_graphs(n)

    print(f"Sub-graphs number = {len(sub_graphs)}\n")
    if len(sub_graphs) < 14:
        print(sub_graphs)
    else:
        print(sub_graphs[:7])
        print("....")
        print(sub_graphs[-7:])

    print(f"\n----------------connected_sub_graphs------------------")
    connected_sub_graphs = remove_not_connected_graphs(sub_graphs)

    print(f"Connected sub graphs number = {len(connected_sub_graphs)}\n")
    if len(connected_sub_graphs) < 14:
        print(connected_sub_graphs)
    else:
        print(connected_sub_graphs[:7])
        print("....")
        print(connected_sub_graphs[-7:])

    print(f"\n--------connected_anti_isomorphic_sub_graphs-----------")
    connected_anti_isomorphic_sub_graphs = remove_isomorphic_graphs(connected_sub_graphs)

    print(f"Anti isomorphic connected sub graphs number = {len(connected_anti_isomorphic_sub_graphs)}\n")
    if len(connected_anti_isomorphic_sub_graphs) < 14:
        print(connected_anti_isomorphic_sub_graphs)
    else:
        print(connected_anti_isomorphic_sub_graphs[:7])
        print("....")
        print(connected_anti_isomorphic_sub_graphs[-7:])

    return connected_anti_isomorphic_sub_graphs


def get_all_connected_graphs(n):
    # input: int n
    # output: all connected graphs with n vertices
    if not n:
        return []

    sub_graphs = get_all_graphs(n)

    connected_sub_graphs = remove_not_connected_graphs(sub_graphs)

    connected_anti_isomorphic_sub_graphs = remove_isomorphic_graphs(connected_sub_graphs)

    return connected_anti_isomorphic_sub_graphs


def get_edges(graph):
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            edges.append((vertex, neighbor))
    return edges


def get_all_vertices_subsets(n):
    if n == 0:
        return [[]]
    prev_all_vertices_subsets = get_all_vertices_subsets(n - 1)

    new_all_vertices_subsets = []
    for subset in prev_all_vertices_subsets:
        new_all_vertices_subsets.append(subset)

    for subset in prev_all_vertices_subsets:
        new_all_vertices_subsets.append(subset+[n])

    return new_all_vertices_subsets


def get_all_graphs(n):

    if not n:
        return []
    if n == 1:
        return [{1: []}]
    new_sub_graphs = []
    prev_sub_graphs = get_all_graphs(n-1)
    target_subsets = get_all_vertices_subsets(n-1)
    source_subsets = copy.deepcopy(target_subsets)
    source_subsets.remove([])

    for sources in source_subsets:
        for targets in target_subsets:
            new_sub_graphs += add_new_v_as_source_or_target_to_subset(prev_sub_graphs, sources, targets, n)

    return new_sub_graphs


def add_new_v_as_source_or_target_to_subset(graphs, sources, targets, new_v):
    # add new_v as target to sources
    graphs_with_new_v_as_target = copy.deepcopy(graphs)
    for graph in copy.deepcopy(graphs):
        for s in sources:
            graph_v = graph.get(s, 0)
            if new_v not in graph_v:
                graph[s] = graph_v + [new_v]
        graphs_with_new_v_as_target += [graph]

    graphs_with_new_v_as_target_or_source = []

    # add new_v as source to targets
    for graph in copy.deepcopy(graphs_with_new_v_as_target):
        graph[new_v] = targets
        graphs_with_new_v_as_target_or_source += [graph]

    return graphs_with_new_v_as_target_or_source


def write_all_graphs_of_size_n_to_file(n):
    text = ""

    text += f"{n=}\n"

    all_sub_graphs = run_with_saving_computation_time(n)

    text += f"count={len(all_sub_graphs)}\n"
    for i, sub_graphs in enumerate(all_sub_graphs):
        text += f"#{i+1}\n"
        for edge in get_edges(sub_graphs):
            text += f"{edge[0]} {edge[1]}\n"

    file_path = f"all_sub_graphs_of_size_{n}"
    with open(file_path, 'w') as file:
        file.write(text)

    # print(text)


def count_motifs_in_graph(graph_string, n):
    g = convert_graph_string_to_dict(graph_string)

    all_motifs = get_all_connected_graphs(n)  #_with_print

    # print(f"{all_motifs=}")
    # print(f"{len(all_motifs)=}")

    # print(f"{all_motifs=}")

    all_sub_graphs = get_all_sub_graphs(g)
    all_sub_graphs.remove({})
    # print(f"{g=}")
    # print(f"{all_sub_graphs=}")

    all_motifs_counter = [0 for motif in all_motifs]
    for sub_graph in all_sub_graphs:
        for i, motif in enumerate(all_motifs):
            if is_isomorphic(sub_graph, motif):
                all_motifs_counter[i] += 1
                break
    # print(all_motifs)
    # print(all_motifs_counter)
    # for i in range(len(all_motifs)):
    #     print(f"##{i+1} Motif: {all_motifs[i]} is showing {all_motifs_counter[i]} times")

    return all_motifs, all_motifs_counter


def get_all_sub_graphs(graph):
    max_v = max(graph.keys())
    all_vertices_subsets = get_all_vertices_subsets(max_v)
    all_sub_graphs = []
    for vertices_subset in all_vertices_subsets:
        sub_graph = {}
        for v in vertices_subset:
            sub_graph[v] = []
        for v in sub_graph:
            sub_graph[v] = [u for u in graph[v] if u in sub_graph]
        all_sub_graphs.append(copy.deepcopy(sub_graph))
    return all_sub_graphs


def convert_graph_string_to_dict(graph_string):
    graph_dict = {}

    # Split the string into lines
    lines = graph_string.strip().split('\n')

    for line in lines:
        # Split each line into source and destination vertices
        source, destination = map(int, line.split())

        # Add the source vertex to the dictionary if it doesn't exist
        if source not in graph_dict:
            graph_dict[source] = []

        # Add the destination vertex to the source's list of neighbors
        graph_dict[source].append(destination)

        # Add the destination vertex to the dictionary if it doesn't exist
        if destination not in graph_dict:
            graph_dict[destination] = []

    return graph_dict


def write_sub_graphs_of_size_n_counting_to_file(graph_str, n):

    all_motifs, all_motifs_counter = count_motifs_in_graph(graph_str, n)
    text = ""
    text += f"{n=}\n"

    for i in range(len(all_motifs)):
        text += f"#{i+1}\n"
        text += f"count={all_motifs_counter[i]}\n"
        for edge in get_edges(all_motifs[i]):
            text += f"{edge[0]} {edge[1]}\n"

    file_path = f"sub_graphs_of_size_{n}_counting"
    with open(file_path, 'w') as file:
        file.write(text)


computation_times = {}


def run_with_saving_computation_time(n):
    # Measure the time taken by your program for a given value of n

    start_time = time.time()
    start_date = datetime.now().strftime("%H:%M:%S")

    all_sub_graphs = get_all_connected_graphs_with_print(n)

    finish_date = datetime.now().strftime("%H:%M:%S")
    computation_time = time.time() - start_time
    computation_times[n] = {"Start Time": start_date, "Finish Time": finish_date, "Computation Time": computation_time}

    return all_sub_graphs


def get_graph_from_user():

    continue_char = "y"
    i = 1
    graph = {}
    while continue_char == "y":
        s = int(input(f"Enter the source of edge {i}:"))
        t = int(input(f"Enter the target of edge {i}:"))

        if t in graph.get(s, []):
            print("Existing edge, try again!")
        else:
            graph[s] = graph.get(s, []) + [t]
            i += 1
            print(f"The graph:\n {graph}")
            continue_char = input("Do you want to add another edge to the graph? y/[n]")

    return graph


def convert_dict_to_graph_string(graph_dict):
    graph_string = ""

    for source, destinations in graph_dict.items():
        for destination in destinations:
            graph_string += f"{source} {destination}\n"

    return graph_string


if __name__ == "__main__":

    print("\n#  ------------------- 1 --------------------- #")
    print("Generate all connected sub-graphs of size n (for each n between 0 to 4)\n")

    for n in range(5):
        write_all_graphs_of_size_n_to_file(n)

    for n in range(5):
        print(f"\n----- {n=} -----")
        print("Start Time =", computation_times[n]["Start Time"])
        print("Finish Time =", computation_times[n]["Finish Time"])
        print(f"The computation time for {n=} is ", computation_times[n]["Computation Time"], " seconds")

    print("\n\n#  ------------------- 2 --------------------- #")
    print("Program that gets as input positive integer n and a graph \n"
          "and outputs all sub-graphs of size n and count how many instances appear of each motif\n")

    ans = input("Enter 1 for hard-coded graph example\n"
                "   or 2 for insert graph manually\n")

    if ans == "1":
        graph_str1 = '''
        1 2
        2 3
        1 3
        3 4
        '''
        print(f"The given graph is:\n {graph_str1}")
        print("Computing...")
        for n in range(5):
            print(f"   for {n=}...")
            write_sub_graphs_of_size_n_counting_to_file(graph_str1, n)

    elif ans == "2":
        graph_dict = get_graph_from_user()
        graph_str = convert_dict_to_graph_string(graph_dict)
        print("\nGraph in format:")
        print(graph_str)

        print("Computing...")
        for n in range(5):
            print(f"   for {n=}...")
            write_sub_graphs_of_size_n_counting_to_file(graph_str, n)

    print("\nThe results are in the files 'sub_graphs_of_size_n_counting' (for each n between 0 to 4)")



