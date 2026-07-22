"""
Visualization module for PageRank:

This module provides functions to visualize a directed graph with node sizes
and colors proportional to PageRank scores, and to compare graphs before and
after removing a node (attack simulation).
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import networkx as nx
import numpy as np


def draw_graph(G, ranks):
    """
    Draw a directed graph with node size and color representing PageRank scores.

    Parameters:

    G : networkx.DiGraph
        The directed graph to visualize.
    ranks : list or numpy.ndarray
        PageRank scores for each node (order must match G.nodes()).
    """
    # Create a new figure with a specific size
    plt.figure(figsize=(9, 7))

    # Compute a consistent layout using spring layout with a fixed seed for reproducibility
    pos = nx.spring_layout(G, seed=42)

    # Get the list of nodes in the graph
    nodes = list(G.nodes())

    # Identify the node with the highest PageRank
    top_node = nodes[np.argmax(ranks)]

    # Set edge colors: gold for the highest-ranked node, black for others
    edge_colors = []
    for node in nodes:
        if node == top_node:
            edge_colors.append("gold")
        else:
            edge_colors.append("black")

    # Scale node sizes based on PageRank (larger score => larger node)
    node_sizes = [4000 * r + 500 for r in ranks]

    # Normalize rank values for color mapping
    norm = colors.Normalize(vmin=min(ranks), vmax=max(ranks))

    # Draw nodes with colors mapped to ranks and sizes proportional to ranks
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        node_color=ranks,
        cmap=plt.cm.viridis,
        edgecolors=edge_colors,
        linewidths=3
    )

    # Draw directed edges
    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=20,
        width=2
    )

    # Create labels showing node name and its PageRank score
    labels = {node: f"{node}\n{ranks[i]:.3f}" for i, node in enumerate(nodes)}
    nx.draw_networkx_labels(
        G,
        pos,
        labels,
        font_size=10,
        font_weight="bold"
    )

    # Add a colorbar for the PageRank scores
    sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=plt.gca(), label="PageRank Score")

    # Set title and remove axes
    plt.title("PageRank Visualization", fontsize=16, fontweight="bold")
    plt.axis("off")

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig("outputs/pagerank_graph.png", dpi=300, bbox_inches="tight")
    plt.show()


def compare_graphs(G_before, rank_before, G_after, rank_after, removed_node):
    """
    Draw two side-by-side graphs: original network and network after removing a node.

    Parameters:
    
    G_before : networkx.DiGraph
        Original graph.
    rank_before : list or numpy.ndarray
        PageRank scores for the original graph.
    G_after : networkx.DiGraph
        Graph after node removal.
    rank_after : list or numpy.ndarray
        PageRank scores for the graph after removal.
    removed_node : str
        The node that was removed (highlighted in gold on the left plot).
    """
    print("\nDrawing comparison graph...")

    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Use the same layout for both graphs to make comparison easier
    pos = nx.spring_layout(G_before, seed=42)

    # Combine all ranks to create a unified color scale
    all_ranks = list(rank_before) + list(rank_after)
    norm = colors.Normalize(vmin=min(all_ranks), vmax=max(all_ranks))

    # -------------------- LEFT: BEFORE ATTACK --------------------
    nodes_before = list(G_before.nodes())

    # Node sizes based on ranks
    sizes_before = [4000 * r + 500 for r in rank_before]

    # Highlight the node that will be removed with gold edge color
    edge_colors = []
    for node in nodes_before:
        if node == removed_node:
            edge_colors.append("gold")
        else:
            edge_colors.append("black")

    # Draw nodes for the original graph
    nx.draw_networkx_nodes(
        G_before,
        pos,
        node_size=sizes_before,
        node_color=rank_before,
        cmap=plt.cm.viridis,
        edgecolors=edge_colors,
        linewidths=3,
        ax=axes[0]
    )

    # Draw edges
    nx.draw_networkx_edges(
        G_before,
        pos,
        arrows=True,
        arrowsize=20,
        width=2,
        ax=axes[0]
    )

    # Add labels with scores
    labels_before = {node: f"{node}\n{rank_before[i]:.3f}" for i, node in enumerate(nodes_before)}
    nx.draw_networkx_labels(
        G_before,
        pos,
        labels_before,
        font_size=10,
        font_weight="bold",
        ax=axes[0]
    )

    axes[0].set_title("Before Attack", fontsize=14, fontweight="bold")
    axes[0].axis("off")

    # -------------------- RIGHT: AFTER ATTACK --------------------
    nodes_after = list(G_after.nodes())

    # Keep the same node positions (the removed node is simply absent)
    pos_after = {node: pos[node] for node in nodes_after}

    sizes_after = [4000 * r + 500 for r in rank_after]

    # Draw nodes for the attacked graph
    nx.draw_networkx_nodes(
        G_after,
        pos_after,
        node_size=sizes_after,
        node_color=rank_after,
        cmap=plt.cm.viridis,
        edgecolors="black",
        linewidths=2,
        ax=axes[1]
    )

    # Draw edges
    nx.draw_networkx_edges(
        G_after,
        pos_after,
        arrows=True,
        arrowsize=20,
        width=2,
        ax=axes[1]
    )

    # Add labels with scores
    labels_after = {node: f"{node}\n{rank_after[i]:.3f}" for i, node in enumerate(nodes_after)}
    nx.draw_networkx_labels(
        G_after,
        pos_after,
        labels_after,
        font_size=10,
        font_weight="bold",
        ax=axes[1]
    )

    axes[1].set_title("After Attack", fontsize=14, fontweight="bold")
    axes[1].axis("off")

    # -------------------- SHARED COLORBAR --------------------
    sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=axes, fraction=0.04, pad=0.06)
    cbar.set_label("PageRank Score", fontsize=11)

    # Main title and layout adjustments
    fig.suptitle(
        "Comparison of Network Before and After Removing the Highest Ranked Node",
        fontsize=16,
        fontweight="bold"
    )
    plt.subplots_adjust(wspace=0.25, right=0.88, top=0.88)

    # Save the figure
    plt.savefig("outputs/network_comparison.png", dpi=300, bbox_inches="tight")
    print("Comparison image saved.")

    plt.show()