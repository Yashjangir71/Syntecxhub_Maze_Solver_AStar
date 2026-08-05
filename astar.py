"""
astar.py

This module implements the A* Search Algorithm.
"""

import heapq
from heuristic import manhattan_distance


def get_neighbors(position, maze):
    """
    Returns all valid neighboring cells.
    """

    row, col = position

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    neighbors = []

    rows = len(maze)
    cols = len(maze[0])

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        # Check maze boundaries
        if 0 <= new_row < rows and 0 <= new_col < cols:

            # Ignore walls
            if maze[new_row][new_col] != "#":
                neighbors.append((new_row, new_col))

    return neighbors


def reconstruct_path(came_from, current):
    """
    Reconstructs the shortest path.
    """

    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path


def a_star(maze, start, goal):
    """
    Performs A* Search.

    Returns:
        Shortest path if found.
        None otherwise.
    """

    open_set = []

    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {
        start: 0
    }

    f_score = {
        start: manhattan_distance(start, goal)
    }

    visited = set()

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current, maze):

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score[neighbor] = tentative_g + manhattan_distance(neighbor, goal)

                heapq.heappush(
                    open_set,
                    (f_score[neighbor], neighbor)
                )

    return None