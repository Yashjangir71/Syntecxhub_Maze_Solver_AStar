"""
maze.py

This module loads and displays the maze.
"""

def load_maze(filename):
    """
    Reads a maze from a text file.

    Symbols:
    S = Start
    G = Goal
    # = Wall
    . = Empty Cell
    """

    maze = []

    allowed = set(["S", "G", ".", "#"])

    with open(filename, "r") as file:
        for line in file:
            s = line.strip()

            if not s:
                continue

            # Only include lines that contain maze characters
            if all(ch in allowed for ch in s):
                maze.append(list(s))

    return maze


def find_position(maze, symbol):
    """
    Finds the position of a symbol in the maze.
    """

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == symbol:
                return (row, col)

    return None


def print_maze(maze):
    """
    Prints the maze.
    """

    for row in maze:
        print(" ".join(row))


def mark_path(maze, path):
    """
    Marks the shortest path using '*'
    """

    for row, col in path:

        if maze[row][col] not in ("S", "G"):
            maze[row][col] = "*"