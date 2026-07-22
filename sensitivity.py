"""
Sensitivity Analysis Module

This module provides a function to perform sensitivity analysis on a graph
by removing each node individually and measuring the impact on PageRank scores.
"""

import networkx as nx
import numpy as np

from graph_utils import adjacency_matrix, transition_matrix
from pagerank import pagerank


def sensitivity_analysis(G):
    """
    Perform sensitivity analysis by removing each nod one at a time:

    For each node in the graph:
        - Remove the node.
        - Compute PageRank on the reduced graph.
        - Measure the mean absolute change in scores of the remaining nodes.
        - Store the impact score.

    The results are sorted in descending order of impact.

    Parameters: 
    
    G : networkx.DiGraph
        The directed graph to analyze.

    Returns
    -------
    impacts : list of tuples
        Each tuple contains (node_name, impact_score), sorted from highest impact.
    """
    print("\n" + "=" * 50)
    print("        SENSITIVITY ANALYSIS")
    print("=" * 50)

    # Compute original PageRank for reference
    A, nodes = adjacency_matrix(G)
    T = transition_matrix(A)
    original_rank = pagerank(T)

    impacts = []

    # Iterate over each node to simulate its removal
    for removed_node in nodes:
        # Create a copy of the graph and remove the node
        temp_graph = G.copy()
        temp_graph.remove_node(removed_node)

        # Build new adjacency and transition matrices
        A2, nodes2 = adjacency_matrix(temp_graph)
        T2 = transition_matrix(A2)

        # Compute PageRank on the reduced graph
        new_rank = pagerank(T2)

        # Find nodes that are common in both original and reduced graphs
        common_nodes = [node for node in nodes if node != removed_node]

        old_scores = []
        new_scores = []

        for node in common_nodes:
            old_scores.append(original_rank[nodes.index(node)])
            new_scores.append(new_rank[nodes2.index(node)])

        # Compute mean absolute change in PageRank scores
        impact = np.mean(np.abs(np.array(old_scores) - np.array(new_scores)))
        impacts.append((removed_node, impact))

    # Sort impacts in descending order (highest impact first)
    impacts.sort(key=lambda x: x[1], reverse=True)

    # Print a formatted table
    print()
    print("Node      Impact Score")
    print("-" * 28)
    for node, score in impacts:
        print(f"{node:<8}{score:.5f}")

    return impacts