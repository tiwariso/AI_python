# -*- coding: utf-8 -*-
"""C3_42_AI_practical_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10WBjbDlE-9VsKurZ2x3oUm54rTNi5IMF
"""

from queue import PriorityQueue

def greedy_best_first_search(graph, heuristics, start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristics[start], start))
    closed_list = set()
    came_from = {}

    while not open_list.empty():
        current_priority, current_node = open_list.get()
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor in closed_list:
                continue
            if neighbor not in [i[1] for i in open_list.queue]:
                came_from[neighbor] = current_node
                open_list.put((heuristics[neighbor], neighbor))

    return None

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

heuristics = {
    'A': 13,
    'B': 12,
    'C': 4,
    'D': 7,
    'E': 3,
    'F': 8,
    'G': 2,
    'H': 0
}

start = 'A'
goal = 'H'
path = greedy_best_first_search(graph, heuristics, start, goal)
print("Path:", path)

import heapq

def a_star_algorithm(start, stop, graph, heuristics):


    open_list = []
    closed_list = set()


    heapq.heappush(open_list, (0 + heuristics[start], start, 0, None))

    while open_list:
        _, current_node, current_cost, parent = heapq.heappop(open_list)

        if current_node in closed_list:
            continue

        closed_list.add(current_node)


        if current_node == stop:
            path = []
            while parent is not None:
                path.append(current_node)
                current_node, _, parent = parent
            path.append(start)
            return path[::-1], current_cost

        for neighbor, weight in graph[current_node]:
            if neighbor in closed_list:
                continue


            total_cost = current_cost + weight
            estimated_cost = total_cost + heuristics[neighbor]

            heapq.heappush(open_list, (estimated_cost, neighbor, total_cost, (current_node, total_cost, parent)))

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 2), ('H', 7)],
    'B': [('D', 4), ('E', 6)],
    'C': [('F', 3), ('G', 2)],
    'D': [('E', 7)],
    'E': [],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

heuristics = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 6,
    'F': 3,
    'G': 1,
    'H': 0
}

start = 'A'
goal = 'H'
path, cost = a_star_algorithm(start, goal, graph, heuristics)
print(f"Path: {path}, Cost: {cost}")

