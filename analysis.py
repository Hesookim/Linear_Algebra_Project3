import numpy as np


def network_report(
    original_nodes,
    original_rank,
    removed_node,
    attacked_nodes,
    attacked_rank,
    personalized_rank,
    start_node
):

    print("\n" + "=" * 50)
    print("        NETWORK ANALYSIS REPORT")
    print("=" * 50)

    # Original top node
    top_original = original_nodes[np.argmax(original_rank)]

    print(f"\nOriginal Top Node       : {top_original}")

    print(f"Removed Node            : {removed_node}")

    # New top node
    top_after = attacked_nodes[np.argmax(attacked_rank)]

    print(f"Top Node After Attack   : {top_after}")

    # Personalized top node
    top_personal = original_nodes[np.argmax(personalized_rank)]

    print(f"Personalized Start Node : {start_node}")
    print(f"Personalized Top Node   : {top_personal}")

    # Average rank change
    common_nodes = [
        node for node in original_nodes
        if node != removed_node
    ]

    old_scores = []

    new_scores = []

    for node in common_nodes:

        old_scores.append(
            original_rank[
                original_nodes.index(node)
            ]
        )

        new_scores.append(
            attacked_rank[
                attacked_nodes.index(node)
            ]
        )

    average_change = np.mean(
        np.abs(
            np.array(old_scores) -
            np.array(new_scores)
        )
    )

    print(f"\nAverage Rank Change : {average_change:.5f}")

    # Impact level
    if average_change > 0.10:
        impact = "HIGH"

    elif average_change > 0.05:
        impact = "MEDIUM"

    else:
        impact = "LOW"

    print(f"Impact Level        : {impact}")

    print("\nInterpretation:")

    print(
        f"The removal of node '{removed_node}' changed the ranking of the remaining nodes."
    )

    print(
        f"The Personalized PageRank starting from '{start_node}' increased the importance of nearby nodes."
    )

    print("=" * 50)