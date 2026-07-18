import networkx as nx
import numpy as np

from graph_utils import adjacency_matrix, transition_matrix
from pagerank import pagerank


def sensitivity_analysis(G):

    print("\n" + "=" * 50)
    print("        SENSITIVITY ANALYSIS")
    print("=" * 50)

    # Original ranking
    A, nodes = adjacency_matrix(G)
    T = transition_matrix(A)

    original_rank = pagerank(T)

    impacts = []

    for removed_node in nodes:

        temp_graph = G.copy()
        temp_graph.remove_node(removed_node)

        A2, nodes2 = adjacency_matrix(temp_graph)
        T2 = transition_matrix(A2)

        new_rank = pagerank(T2)

        common_nodes = [
            node for node in nodes
            if node != removed_node
        ]

        old_scores = []

        new_scores = []

        for node in common_nodes:

            old_scores.append(
                original_rank[
                    nodes.index(node)
                ]
            )

            new_scores.append(
                new_rank[
                    nodes2.index(node)
                ]
            )

        impact = np.mean(
            np.abs(
                np.array(old_scores) -
                np.array(new_scores)
            )
        )

        impacts.append(
            (
                removed_node,
                impact
            )
        )

    impacts.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print()

    print("Node      Impact Score")

    print("-" * 28)

    for node, score in impacts:

        print(
            f"{node:<8}{score:.5f}"
        )

    return impacts