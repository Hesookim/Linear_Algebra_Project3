"""
Graph Utilities Module:

This module provides utility functions for creating a sample directed graph,
converting it to an adjacency matrix, and constructing a column stochastic
transition matrix for PageRank computations.
"""

import networkx as nx
import numpy as np


def create_sample_graph():
    """
    Create a sample directed graph for testing PageRank:

    The graph consists of 5 nodes (A, B, C, D, E) with the following edges:
        A → B, C
        B → C
        C → A
        D → C
        E → C, D

    Returns: 
    G : networkx.DiGraph
        A directed graph object.
    """
    G = nx.DiGraph()

    # Define directed edges
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("C", "A"),
        ("D", "C"),
        ("E", "C"),
        ("E", "D")
    ]

    G.add_edges_from(edges)
    return G


def adjacency_matrix(G):
    """
    Convert a NetworkX graph to an adjacency matrix:

    The adjacency matrix A has A[i, j] = 1 if there is an edge from node j to node i
    (column‑oriented representation), following the convention used in PageRank:

    Parameters: 

    G : networkx.DiGraph
        The directed graph.

    Returns: 

    A : numpy.ndarray
        Adjacency matrix (n x n) with binary entries.
    nodes : list
        List of node names in the order they appear in the matrix.
    """
    nodes = list(G.nodes())

    # Convert graph to numpy array with specified node order
    A = nx.to_numpy_array(G, nodelist=nodes, dtype=float)

    return A, nodes


def transition_matrix(A):
    """
    Convert an adjacency matrix to a column‑stochastic transition matrix.

    For each column j (representing node j):
        - If the column sum > 0, divide each entry by the column sum.
        - If the column sum == 0 (dangling node with no outgoing edges),
          set the entire column to 1/n (uniform teleportation probability).

    This produces a matrix T where T[i, j] = P(transition from j to i).

    Parameters:

    A : numpy.ndarray
        Adjacency matrix (n x n), with A[i, j] = 1 if edge j → i exists.

    Returns:
    
    T : numpy.ndarray
        Column‑stochastic transition matrix.
    """
    T = A.copy()
    n = T.shape[0]

    # Normalize each column
    for j in range(n):
        column_sum = np.sum(T[:, j])

        if column_sum == 0:
            # Dangling node: no outgoing edges → uniform distribution
            T[:, j] = 1 / n
        else:
            # Normalize the column to sum to 1
            T[:, j] /= column_sum

    return T