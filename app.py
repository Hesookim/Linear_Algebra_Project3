from analysis import network_report
from visualization import draw_graph, compare_graphs
from pagerank import personalized_pagerank
from sensitivity import sensitivity_analysis
from graph_utils import (
    create_sample_graph,
    adjacency_matrix,
    transition_matrix
)

G = create_sample_graph()

A, nodes = adjacency_matrix(G)

T = transition_matrix(A)

print("Nodes:")
print(nodes)

print("\nAdjacency Matrix:")
print(A)

print("\nOutgoing Links:\n")

for i, node in enumerate(nodes):

    print(node, "->", A[i])

print("\nTransition Matrix:")
print(T)

from pagerank import pagerank

rank = pagerank(T)

print("\nPageRank Scores:\n")

for node, score in zip(nodes, rank):

    print(f"{node} : {score:.5f}")

from visualization import draw_graph

draw_graph(G, rank)

from attack_simulation import simulate_attack

removed_node, attacked_graph, attacked_nodes, attacked_ranks = simulate_attack(G)

print("\nNew Ranking After Attack\n")

for node, score in zip(attacked_nodes, attacked_ranks):

    print(f"{node} : {score:.5f}")

compare_graphs(
    G,
    rank,
    attacked_graph,
    attacked_ranks,
    removed_node
)


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

network_report(
    nodes,
    rank,
    removed_node,
    attacked_nodes,
    attacked_ranks,
    personal_rank,
    start_node
)

sensitivity_analysis(G)