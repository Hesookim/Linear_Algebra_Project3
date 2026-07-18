import networkx as nx
import numpy as np

from graph_utils import adjacency_matrix, transition_matrix
from pagerank import pagerank


def simulate_attack(G):

    print("\n==============================")
    print("ATTACK SIMULATION")
    print("==============================")

    # Original graph
    A, nodes = adjacency_matrix(G)
    T = transition_matrix(A)

    ranks = pagerank(T)

    index = np.argmax(ranks)

    removed_node = nodes[index]

    print(f"\nMost Important Node : {removed_node}")

    # Remove node
    attacked_graph = G.copy()

    attacked_graph.remove_node(removed_node)

    A2, nodes2 = adjacency_matrix(attacked_graph)

    T2 = transition_matrix(A2)

    new_ranks = pagerank(T2)

    return (
        removed_node,
        attacked_graph,
        nodes2,
        new_ranks
    )