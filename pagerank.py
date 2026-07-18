import numpy as np


def pagerank(
    T,
    damping=0.85,
    tolerance=1e-8,
    max_iterations=100
):
    """
    Compute PageRank using Power Iteration.
    """

    n = T.shape[0]

    rank = np.ones(n) / n

    teleport = np.ones(n) / n

    for iteration in range(max_iterations):

        new_rank = (
            damping * (T @ rank)
            + (1 - damping) * teleport
        )

        # Adaptive Convergence
        if np.linalg.norm(new_rank - rank, ord=1) < tolerance:

            print(f"Converged after {iteration+1} iterations")

            return new_rank

        rank = new_rank

    print("Reached maximum iterations")

    return rank

def personalized_pagerank(
    T,
    start_node,
    nodes,
    damping=0.85,
    tolerance=1e-8,
    max_iterations=100
):

    n = len(nodes)

    teleport = np.zeros(n)

    teleport[nodes.index(start_node)] = 1

    rank = np.ones(n) / n

    for iteration in range(max_iterations):

        new_rank = (
            damping * (T @ rank)
            + (1 - damping) * teleport
        )

        if np.linalg.norm(
            new_rank-rank,
            ord=1
        ) < tolerance:

            print(
                f"\nPersonalized PageRank converged after {iteration+1} iterations"
            )

            return new_rank

        rank = new_rank

    return rank