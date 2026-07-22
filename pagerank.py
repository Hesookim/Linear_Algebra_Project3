"""
PageRank Algorithm Module:

This module implements the standard PageRank and Personalized PageRank
algorithms using the power iteration method.
"""

import numpy as np


def pagerank(T, damping=0.85, tolerance=1e-8, max_iterations=100):
    """
    Compute PageRank scores using the power iteration method:

    The PageRank algorithm iteratively computes the stationary distribution
    of a random walk on a directed graph with teleportation.

    Parameters:

    T : numpy.ndarray
        Column‑stochastic transition matrix (each column sums to 1).
        T[i, j] is the probability of transitioning from node j to node i.
    damping : float, default=0.85
        Damping factor (probability of following links vs teleporting).
    tolerance : float, default=1e-8
        Convergence tolerance (L1 norm of change between iterations).
    max_iterations : int, default=100
        Maximum number of iterations before giving up.

    Returns:

    rank : numpy.ndarray
        PageRank scores for each node (sums to 1).
    """
    # Number of nodes
    n = T.shape[0]

    # Initialize the rank vector uniformly
    rank = np.ones(n) / n

    # Teleport vector: uniform distribution (standard PageRank)
    teleport = np.ones(n) / n

    # Power iteration loop
    for iteration in range(max_iterations):
        # Update rank: rank = damping * T @ rank + (1 - damping) * teleport
        new_rank = (damping * (T @ rank) + (1 - damping) * teleport)

        # Check convergence using L1 norm
        if np.linalg.norm(new_rank - rank, ord=1) < tolerance:
            print(f"Converged after {iteration+1} iterations")
            return new_rank

        rank = new_rank

    # If loop completes without convergence
    print("Reached maximum iterations")
    return rank


def personalized_pagerank(T, start_node, nodes, damping=0.85, tolerance=1e-8, max_iterations=100):
    """
    Compute Personalized PageRank scores:

    Personalized PageRank biases the random walk toward a specific starting node
    by setting the teleport vector to a one‑hot distribution at that node.

    Parameters:

    T : numpy.ndarray
        Column‑stochastic transition matrix.
    start_node : str
        The node to personalize the teleport vector to.
    nodes : list of str
        List of node names in the order they appear in T.
    damping : float, default=0.85
        Damping factor.
    tolerance : float, default=1e-8
        Convergence tolerance.
    max_iterations : int, default=100
        Maximum number of iterations.

    Returns:
    
    rank : numpy.ndarray
        Personalized PageRank scores (sums to 1).
    """
    n = len(nodes)

    # Create teleport vector: 1 at the start_node, 0 elsewhere
    teleport = np.zeros(n)
    teleport[nodes.index(start_node)] = 1

    # Initialize rank uniformly
    rank = np.ones(n) / n

    # Power iteration loop
    for iteration in range(max_iterations):
        new_rank = (damping * (T @ rank) + (1 - damping) * teleport)

        if np.linalg.norm(new_rank - rank, ord=1) < tolerance:
            print(f"\nPersonalized PageRank converged after {iteration+1} iterations")
            return new_rank

        rank = new_rank

    return rank