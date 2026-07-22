"""
Main Application Script for PageRank Analysis:

This script orchestrates the entire PageRank analysis pipeline:
    - Creates a sample directed graph.
    - Builds adjacency and transition matrices.
    - Computes standard PageRank.
    - Visualizes the graph with PageRank scores.
    - Simulates an attack (removes the most important node).
    - Compares the network before and after the attack.
    - Computes personalized PageRank.
    - Generates a comprehensive network report.
    - Performs sensitivity analysis.
"""

from analysis import network_report
from visualization import draw_graph, compare_graphs
from pagerank import personalized_pagerank
from sensitivity import sensitivity_analysis
from graph_utils import (
    create_sample_graph,
    adjacency_matrix,
    transition_matrix
)

# Create the graph and its matrix representations

# Create a sample directed graph (5 nodes: A, B, C, D, E)
G = create_sample_graph()

# Build adjacency matrix (A[i,j] = 1 if edge j → i exists)
A, nodes = adjacency_matrix(G)

# Build column‑stochastic transition matrix (T[i,j] = P(j → i))
T = transition_matrix(A)

# Display basic graph information
print("Nodes:")
print(nodes)

print("\nAdjacency Matrix:")
print(A)

print("\nOutgoing Links:\n")
for i, node in enumerate(nodes):
    print(node, "->", A[i])  # Column i shows outgoing links from node i

print("\nTransition Matrix:")
print(T)

# Compute standard PageRank



from pagerank import pagerank

rank = pagerank(T)

print("\nPageRank Scores:\n")
for node, score in zip(nodes, rank):
    print(f"{node} : {score:.5f}")

# Visualize the original graph

from visualization import draw_graph
draw_graph(G, rank)  # Saves "outputs/pagerank_graph.png" and shows the plot


#Simulate an attack (remove the highest‑ranked node)

from attack_simulation import simulate_attack

removed_node, attacked_graph, attacked_nodes, attacked_ranks = simulate_attack(G)

print("\nNew Ranking After Attack\n")
for node, score in zip(attacked_nodes, attacked_ranks):
    print(f"{node} : {score:.5f}")

#  Compare graphs before and after attack

compare_graphs(
    G,
    rank,
    attacked_graph,
    attacked_ranks,
    removed_node
)  # Saves "outputs/network_comparison.png"

# Compute Personalized PageRank

print("\n==============================")
print("PERSONALIZED PAGERANK")
print("==============================")

start_node = "A"

personal_rank = personalized_pagerank(
    T,
    start_node,
    nodes
)

print(f"\nStarting Node : {start_node}\n")
for node, score in zip(nodes, personal_rank):
    print(f"{node} : {score:.5f}")

#  Generate network analysis report

network_report(
    nodes,
    rank,
    removed_node,
    attacked_nodes,
    attacked_ranks,
    personal_rank,
    start_node
)

# Sensitivity analysis

sensitivity_analysis(G)  # Prints impact scores and returns results