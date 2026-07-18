import matplotlib.pyplot as plt
import matplotlib.colors as colors
import networkx as nx
import numpy as np


def draw_graph(G, ranks):

    plt.figure(figsize=(9, 7))

    # Graph layout
    pos = nx.spring_layout(
        G,
        seed=42
    )

    nodes = list(G.nodes())

    # Highest ranked node
    top_node = nodes[np.argmax(ranks)]

    edge_colors = []

    for node in nodes:

        if node == top_node:
            edge_colors.append("gold")
        else:
            edge_colors.append("black")

    # Node size based on PageRank
    node_sizes = [
        4000 * r + 500
        for r in ranks
    ]

    # Normalize colors
    norm = colors.Normalize(
        vmin=min(ranks),
        vmax=max(ranks)
    )

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        node_color=ranks,
        cmap=plt.cm.viridis,
        edgecolors=edge_colors,
        linewidths=3
    )

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=20,
        width=2
    )

    # Labels
    labels = {
        node: f"{node}\n{ranks[i]:.3f}"
        for i, node in enumerate(nodes)
    }

    nx.draw_networkx_labels(
        G,
        pos,
        labels,
        font_size=10,
        font_weight="bold"
    )

    # Colorbar
    sm = plt.cm.ScalarMappable(
        cmap=plt.cm.viridis,
        norm=norm
    )

    sm.set_array([])

    plt.colorbar(
        sm,
        ax=plt.gca(),
        label="PageRank Score"
    )

    plt.title(
        "PageRank Visualization",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "outputs/pagerank_graph.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

def compare_graphs(
    G_before,
    rank_before,
    G_after,
    rank_after,
    removed_node
):

    print("\nDrawing comparison graph...")

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(16, 7)
    )

    # Use SAME layout for both graphs
    pos = nx.spring_layout(
        G_before,
        seed=42
    )

    all_ranks = list(rank_before) + list(rank_after)

    norm = colors.Normalize(
        vmin=min(all_ranks),
        vmax=max(all_ranks)
    )

    ###################################################
    # BEFORE ATTACK
    ###################################################

    nodes_before = list(G_before.nodes())

    sizes_before = [
        4000 * r + 500
        for r in rank_before
    ]

    edge_colors = []

    for node in nodes_before:

        if node == removed_node:
            edge_colors.append("gold")
        else:
            edge_colors.append("black")

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

    nx.draw_networkx_edges(
        G_before,
        pos,
        arrows=True,
        arrowsize=20,
        width=2,
        ax=axes[0]
    )

    labels_before = {
        node: f"{node}\n{rank_before[i]:.3f}"
        for i, node in enumerate(nodes_before)
    }

    nx.draw_networkx_labels(
        G_before,
        pos,
        labels_before,
        font_size=10,
        font_weight="bold",
        ax=axes[0]
    )

    axes[0].set_title(
        "Before Attack",
        fontsize=14,
        fontweight="bold"
    )

    axes[0].axis("off")

    ###################################################
    # AFTER ATTACK
    ###################################################

    nodes_after = list(G_after.nodes())

    # Keep same positions
    pos_after = {
        node: pos[node]
        for node in nodes_after
    }

    sizes_after = [
        4000 * r + 500
        for r in rank_after
    ]

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

    nx.draw_networkx_edges(
        G_after,
        pos_after,
        arrows=True,
        arrowsize=20,
        width=2,
        ax=axes[1]
    )

    labels_after = {
        node: f"{node}\n{rank_after[i]:.3f}"
        for i, node in enumerate(nodes_after)
    }

    nx.draw_networkx_labels(
        G_after,
        pos_after,
        labels_after,
        font_size=10,
        font_weight="bold",
        ax=axes[1]
    )

    axes[1].set_title(
        "After Attack",
        fontsize=14,
        fontweight="bold"
    )

    axes[1].axis("off")

    ###################################################
    # Shared Colorbar
    ###################################################

    sm = plt.cm.ScalarMappable(
        cmap=plt.cm.viridis,
        norm=norm
    )

    sm.set_array([])

    cbar = fig.colorbar(
        sm,
        ax=axes,
        fraction=0.04,
        pad=0.06
    )

    cbar.set_label(
        "PageRank Score",
        fontsize=11
    )

    ###################################################
    # Main Title
    ###################################################

    fig.suptitle(
        "Comparison of Network Before and After Removing the Highest Ranked Node",
        fontsize=16,
        fontweight="bold"
    )

    plt.subplots_adjust(
        wspace=0.25,
        right=0.88,
        top=0.88
    )

    plt.savefig(
        "outputs/network_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Comparison image saved.")

    plt.show()