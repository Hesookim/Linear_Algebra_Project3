"""
Attack Simulation Module:

This module provides a function to simulate an attack on a network by
removing the node with the highest PageRank score and analyzing the impact.
"""

import networkx as nx
import numpy as np

from graph_utils import adjacency_matrix, transition_matrix
from pagerank import pagerank


def simulate_attack(G):
    """
    Simulate an attack by removing the most important node from the network:

    The function:
        1. Computes PageRank on the original graph.
        2. Identifies the node with the highest PageRank score.
        3. Removes that node from the graph.
        4. Computes PageRank on the attacked graph.
        5. Returns the results for further analysis.

    Parameters:

    G : networkx.DiGraph
        The directed graph to attack.

    Returns:

    removed_node : str
        The node that was removed (highest PageRank in original graph).
    attacked_graph : networkx.DiGraph
        The graph after removing the node.
    nodes2 : list
        List of nodes in the attacked graph.
    new_ranks : numpy.ndarray
        PageRank scoress for the attacked graph.
    """
    print("\n========")
    print("ATTACK SIMULATION")
    print("==========")

    #Step 1: Compute original PageRank
    #Build adjacency matrix and transition matrix from the original graph
    A, nodes = adjacency_matrix(G)
    T = transition_matrix(A)

    #Compute PageRank scores
    ranks = pagerank(T)

    #Step 2: Identify the most important node
    #Find the node with the maximum PageRank score
    index = np.argmax(ranks)
    removed_node = nodes[index]
    print(f"\nMost Important Node : {removed_node}")

    #Step 3: Remove the node from the graph
    #Create a copy to avoid modifying the original graph
    attacked_graph = G.copy()
    attacked_graph.remove_node(removed_node)

    #Step 4: Compute PageRank on the attacked graph
    #Build adjacency and transition matrices for the reduced graph
    A2, nodes2 = adjacency_matrix(attacked_graph)
    T2 = transition_matrix(A2)

    #Compute new PageRank scores
    new_ranks = pagerank(T2)

    #Step 5: Return results for further analysis
    return (
        removed_node,      # The node that was removed
        attacked_graph,    # The graph after removal
        nodes2,            # Nodes in the attacked graph
        new_ranks          # New PageRank scores
    )