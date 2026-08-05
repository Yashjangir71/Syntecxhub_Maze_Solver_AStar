"""
main.py

Main program to run the Maze Solver using A* Search.
"""

from maze import (
    load_maze,
    find_position,
    print_maze,
    mark_path
)

from astar import a_star


def main():

    # Load the maze
    maze = load_maze("sample_maze.txt")

    # Find Start and Goal positions
    start = find_position(maze, "S")
    goal = find_position(maze, "G")

    # Validate maze
    if start is None or goal is None:
        print("Error: Maze must contain both 'S' (Start) and 'G' (Goal).")
        return

    print("\nOriginal Maze:\n")
    print_maze(maze)

    # Run A* Search
    path = a_star(maze, start, goal)

    if path:

        print("\nShortest Path Found!\n")

        # Mark the shortest path
        mark_path(maze, path)

        print_maze(maze)

        print("\nPath Coordinates:")

        for node in path:
            print(node)

        print(f"\nTotal Steps: {len(path) - 1}")

    else:

        print("\nNo path found from Start to Goal.")


if __name__ == "__main__":
    main()