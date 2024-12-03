import sys
import os
import time
import argparse
from progress import Progress

import random


def load_graph(args):
    """Load graph from text file

    Parameters:
    args -- arguments named tuple

    Returns:
    A dict mapling a URL (str) to a list of target URLs (str).
    """
    graph = {}
    # Iterate through the file line by line
    for line in args.datafile:
        # And split each line into two URLs
        node, target = line.split()
        graph.setdefault(node, []).append(target)
    return graph


def print_stats(graph):
        """Print number of nodes and edges in the given graph"""
        nodes = len(graph)
        print("Number of nodes: ",nodes)
        edges = sum(len(targets) for targets in graph.values())
        print("Number of edges:", edges)
        


def stochastic_page_rank(graph, args):
    """Stochastic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its hit frequency

    This function estimates the Page Rank by counting how frequently
    a random walk that starts on a random node will after n_steps end
    on each node of the given graph.
    """
    #Initialize the hit count to 0 for each node
    hit_count = {node: 0 for node in graph}

    #Select a random node
    current_node = random.choice(list(graph.keys()))
    hit_count[current_node] += 1

    for i in range(args.steps):
        if current_node not in graph or len(graph[current_node]) == 0:
            current_node = random.choice(list(graph.keys()))
        else: 
            current_node = random.choice(graph[current_node])
        hit_count[current_node] += 1

    #Calculate the hit frequency for each node
    total_hits = sum(hit_count.values())
    hit_frequency = {node: hits / total_hits for node, hits in hit_count.items()}

    return hit_frequency
    


def distribution_page_rank(graph, args):
    """Probabilistic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its probability to be reached

    This function estimates the Page Rank by iteratively calculating
    the probability that a random walker is currently on any node.
    """

    #If distribution repeats a lot, algorithm takes a long time to run
    if algorithm == distribution_page_rank:
        if args.repeats > 5000:
            sys.stderr.write("Repeats for distribution page rank must no more than 5,000, use command: -r 5000 \n")
            args.repeats = 5000
            
    node_prob = {node: 1/len(graph) for node in graph}
    for i in range(args.repeats):
        next_prob = {node: 0 for node in graph}
        for node, targets in graph.items():
            for target in targets:
                next_prob[target] += node_prob[node] / len(targets)
        node_prob = next_prob
    return node_prob
    


parser = argparse.ArgumentParser(description="Estimates page ranks from link information")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Textfile of links among web pages as URL tuples")
parser.add_argument('-m', '--method', choices=('stochastic', 'distribution'), default='stochastic',
                    help="selected page rank algorithm")
parser.add_argument('-r', '--repeats', type=int, default=1_000_000, help="number of repetitions")
parser.add_argument('-s', '--steps', type=int, default=100, help="number of steps a walker takes")
parser.add_argument('-n', '--number', type=int, default=20, help="number of results shown")


if __name__ == '__main__':
    args = parser.parse_args()
    algorithm = distribution_page_rank if args.method == 'distribution' else stochastic_page_rank

    graph = load_graph(args)

    print_stats(graph)

    start = time.time()
    ranking = algorithm(graph, args)
    stop = time.time()
    time = stop - start

    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100*v:.2f}\t{k}' for k,v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")
