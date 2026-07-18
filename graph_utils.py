import networkx as nx
import numpy as np


def create_sample_graph():
    """
    Create a directed graph.
    """

    G = nx.DiGraph()

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

    nodes = list(G.nodes())

    A = nx.to_numpy_array(
        G,
        nodelist=nodes,
        dtype=float
    )

    return A, nodes

def transition_matrix(A):
    """
    Convert adjacency matrix to column-stochastic transition matrix.
    """

    T = A.copy()

    n = T.shape[0]

    for j in range(n):

        column_sum = np.sum(T[:, j])

        if column_sum == 0:
            T[:, j] = 1 / n
        else:
            T[:, j] /= column_sum

    return T


