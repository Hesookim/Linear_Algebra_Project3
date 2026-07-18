# PageRank Algorithm Using Linear Algebra

## Project Overview

This project implements the **PageRank algorithm** from scratch using concepts from **Linear Algebra**. The implementation avoids using built-in PageRank functions and instead relies on matrix operations, power iteration, and probability transition matrices.

In addition to the basic PageRank algorithm, several advanced analytical features have been implemented to better demonstrate the mathematical concepts behind ranking algorithms and network analysis.

This project was developed as part of a **Linear Algebra course**.

---

# Objectives

The main objectives of this project are:

- Construct a directed graph.
- Generate the adjacency matrix.
- Compute the transition probability matrix.
- Implement the Power Iteration method.
- Calculate PageRank scores.
- Analyze node importance.
- Simulate attacks on the network.
- Visualize ranking changes before and after attacks.

---

# Project Structure

```
Project3
│
├── app.py
├── graph_utils.py
├── pagerank.py
├── attack_simulation.py
├── analysis.py
├── sensitivity.py
├── visualization.py
│
├── outputs/
│   ├── pagerank_graph.png
│   └── network_comparison.png
│
└── README.md
```

---

# Features

## Core Features

- Directed graph construction
- Adjacency Matrix generation
- Transition Matrix computation
- Power Iteration implementation
- PageRank calculation
- Graph visualization

---

## Advanced Features

### Adaptive Convergence

Instead of always executing a fixed number of iterations, the algorithm automatically stops when the PageRank vector converges below a predefined tolerance.

This improves both computational efficiency and numerical stability.

---

### Attack Simulation

The algorithm automatically identifies the node with the highest PageRank score and removes it from the graph.

The new PageRank values are then recomputed, allowing comparison of network robustness before and after the attack.

---

### Personalized PageRank

Unlike standard PageRank, Personalized PageRank allows ranking to start from a selected node.

This demonstrates how user preference affects the importance of other nodes in the network.

---

### Network Analysis Report

A summary report is generated including:

- Original highest-ranked node
- Removed node
- New highest-ranked node
- Personalized ranking result
- Average rank change
- Network impact level
- Interpretation of the results

---

### Sensitivity Analysis

Each node is removed individually.

The average ranking variation caused by removing that node is measured to estimate its overall importance within the network.

Nodes are then sorted according to their impact score.

---

# Visualization

The project automatically generates visual representations of the network.

## PageRank Visualization

- Node size represents PageRank score.
- Node color represents relative importance.
- The highest-ranked node is highlighted with a gold border.
- A color scale (Colorbar) is included.

---

## Before / After Comparison

A comparison figure is generated showing:

- Original network
- Network after removing the most important node

Both graphs use the same layout to simplify visual comparison.

---

# Mathematical Background

The implementation is based on the following concepts:

- Graph Theory
- Linear Algebra
- Stochastic Matrices
- Eigenvectors
- Markov Chains
- Power Iteration Method

The PageRank vector satisfies

\[
PR = dTPR + (1-d)\frac{1}{N}
\]

where

- **T** is the transition matrix.
- **d** is the damping factor.
- **N** is the number of nodes.

---

# Requirements

Python 3.10+

Required libraries:

```
numpy
networkx
matplotlib
```

Install dependencies using

```bash
pip install numpy networkx matplotlib
```

---

# Running the Project

Run the project using

```bash
python app.py
```

The program will

- construct the graph
- compute PageRank
- display node rankings
- generate graph visualizations
- simulate node attacks
- compute Personalized PageRank
- perform Sensitivity Analysis
- generate the final analysis report

---

# Sample Output

The console output includes

- Adjacency Matrix
- Transition Matrix
- PageRank Scores
- Attack Simulation Results
- Personalized PageRank
- Network Analysis Report
- Sensitivity Analysis

The following images are also generated:

- pagerank_graph.png
- network_comparison.png

---

# Educational Concepts

This project demonstrates practical applications of

- Matrix Multiplication
- Probability Theory
- Eigenvector Computation
- Markov Processes
- Graph Algorithms
- Network Analysis

---

# Possible Future Improvements

Some possible extensions include

- Reading graphs from CSV files
- Interactive graph editor
- Weighted PageRank
- Topic-sensitive PageRank
- Dynamic network updates
- Performance comparison with NetworkX implementation
- GUI using Tkinter or PyQt

---

# Author

**Minoo**

Bachelor of Computer Engineering

Linear Algebra Course Project

2026