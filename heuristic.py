"""
heuristic.py

This module contains the heuristic function used by the
A* Search algorithm.
"""


def manhattan_distance(current, goal):
    """
    Calculates the Manhattan Distance between two points.

    Parameters:
        current : tuple (row, col)
        goal    : tuple (row, col)

    Returns:
        Integer distance
    """

    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def euclidean_distance(current, goal):
    """
    Calculates the Euclidean Distance between two points.

    Parameters:
        current : tuple (row, col)
        goal    : tuple (row, col)

    Returns:
        Float distance
    """

    return ((current[0] - goal[0]) ** 2 +
            (current[1] - goal[1]) ** 2) ** 0.5