from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list
    of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    # g.nodes  # Все узлы графа.
    neighbours = g[start_node]

    path_nodes = []  # Полностью сгоревшие
    visited_nodes = {node: False for node in g.nodes}  # Посещённые узлы.

    wait_nodes = deque()  # Очередь из горящих узлов, ожидающих поджечь своих соседей.
    wait_nodes.append(start_node)  # Добавляем стартовый эл-т в начало очереди.
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.pop()  # Забираем узел из конца очереди.
        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)
                visited_nodes[neighbour] = True

        path_nodes.append(current_node)  # Полностью сожгли.
    print(g, start_node)
    return list(g.nodes)
