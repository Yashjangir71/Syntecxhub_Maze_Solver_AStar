# Maze Solver using A* Search

## Overview

This project implements the **A* Search Algorithm** to find the shortest path in a maze. The maze consists of a Start point, Goal point, walls, and open paths. The algorithm uses the **Manhattan Distance heuristic** to efficiently determine the optimal route.

This project was developed as part of the **Syntecxhub Artificial Intelligence Internship Program**.

---

## Features

- Implements the A* Search Algorithm
- Uses Manhattan Distance heuristic
- Finds the shortest path from Start to Goal
- Handles unreachable goal scenarios
- Simple text-based maze representation
- Console-based output

---

## Project Structure

```
Syntecxhub_Maze_Solver_AStar/
│
├── main.py
├── astar.py
├── heuristic.py
├── maze.py
├── sample_maze.txt
├── requirements.txt
└── README.md
```

---

## Maze Symbols

| Symbol | Meaning |
|--------|---------|
| S | Start Position |
| G | Goal Position |
| # | Wall |
| . | Empty Path |
| * | Shortest Path |

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Syntecxhub_Maze_Solver_AStar.git
```

### 2. Move to the Project Folder

```bash
cd Syntecxhub_Maze_Solver_AStar
```

### 3. Run the Program

```bash
python main.py
```

---

**Repository & Publishing**

- **Repository name suggestion:** `Syntecxhub_Maze_Solver_AStar` (or the name required by your internship).
- To create the GitHub repo locally and push:

```bash
git init
git add .
git commit -m "Initial commit: Maze Solver using A*"
git branch -M main
git remote add origin https://github.com/<your-username>/Syntecxhub_Maze_Solver_AStar.git
git push -u origin main
```

Replace `<your-username>` with your GitHub username and ensure the remote repository exists before pushing.

---

## Example Maze

```
S...#....
.##.#.##.
....#....
###.#.##.
....#....
.######..
.........
.######.#
........G
```

---

## Expected Output

The program will:

- Display the original maze
- Find the shortest path using A*
- Print the solved maze
- Display the path coordinates
- Show the total number of steps

---

## Algorithm Used

The A* Search Algorithm evaluates nodes using:

```
f(n) = g(n) + h(n)
```

Where:

- **g(n)** = Cost from the start node
- **h(n)** = Manhattan Distance heuristic
- **f(n)** = Estimated total cost

---

## Technologies Used

- Python 3
- Heap Queue (`heapq`)
- A* Search Algorithm

---

## Visualization (Optional)

This project includes an optional `pygame`-based visualizer in `visualize.py`.

- Install `pygame` to use the visualizer:

```bash
pip install -r requirements.txt
```

- Run the visualizer:

```bash
python visualize.py
```

- Controls:
	- Play/Pause: Space or click `Play`/`Pause`
	- Step: Right arrow or click `Step`
	- Reset: `R` or click `Reset`
	- Quit: `Esc` or close the window

If you prefer not to install `pygame`, you can still use the CLI solver with `python main.py`.

## Author

Developed as part of the Syntecxhub Artificial Intelligence Internship.