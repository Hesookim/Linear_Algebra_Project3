"""
Network Analysis Report Module

This module provides a function to generate a comprehensive text report
comparing original PageRank, attacked PageRank (after removing a node),
and personalized PageRank.
"""

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
    """
    Generate and print a detailed network analysis report:

    The report includes:
        - The most important node in the original network.
        - Which node was removed.
        - The most important node after the attack.
        - The most important node using personalized PageRank.
        - Average rank change among remaining nodes.
        - Qualitative impact level (HIGH/MEDIUM/LOW).
        - Interpretation of the results.

    Parameterss:

    original_nodes : list
        List of node names in the original graph.
    original_rank : numpy.ndarray
        PageRank scores for the original graph (matching original_nodes order).
    removed_node : str
        The node that was removed in the attack simulation.
    attacked_nodes : list
        List of node names in the graph after removal.
    attacked_rank : numpy.ndarray
        PageRank scores after removal (matching attacked_nodes order).
    personalized_rank : numpy.ndarray
        Personalized PageRank scores for the original nodes.
    start_node : str
        The starting node used for personalized PageRank.
    """
    # Print header
    print("\n" + "=" * 50)
    print("        NETWORK ANALYSIS REPORT")
    print("=" * 50)

    # Find the node with the highest original PageRank
    top_original = original_nodes[np.argmax(original_rank)]
    print(f"\nOriginal Top Node       : {top_original}")

    # Node that was removed
    print(f"Removed Node            : {removed_node}")

    # Find the node with the highest PageRank after the attack
    top_after = attacked_nodes[np.argmax(attacked_rank)]
    print(f"Top Node After Attack   : {top_after}")

    # Find the node with the highest personalized PageRank
    top_personal = original_nodes[np.argmax(personalized_rank)]
    print(f"Personalized Start Node : {start_node}")
    print(f"Personalized Top Node   : {top_personal}")

    # Compute the average change in PageRank scores for nodes that remain after removal
    # Filter out the removed node from the original list
    common_nodes = [node for node in original_nodes if node != removed_node]

    old_scores = []
    new_scores = []

    for node in common_nodes:
        # Get the original score for this node
        old_scores.append(original_rank[original_nodes.index(node)])
        # Get the new score after attack (must find its index in attacked_nodes)
        new_scores.append(attacked_rank[attacked_nodes.index(node)])

    # Calculate mean absolute change
    average_change = np.mean(np.abs(np.array(old_scores) - np.array(new_scores)))
    print(f"\nAverage Rank Change : {average_change:.5f}")

    # Determine qualitative impact level based on threshold
    if average_change > 0.10:
        impact = "HIGH"
    elif average_change > 0.05:
        impact = "MEDIUM"
    else:
        impact = "LOW"
    print(f"Impact Level        : {impact}")

    # Interpretation messages
    print("\nInterpretation:")
    print(
        f"The removal of node '{removed_node}' changed the ranking of the remaining nodes."
    )
    print(
        f"The Personalized PageRank starting frm '{start_node}' increased the importance of nearby nodes."
    )
    print("=" * 50)