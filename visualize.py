"""
visualize.py

Simple pygame visualization for the Maze Solver.

Runs the A* algorithm and displays the maze with the shortest path.
"""

import sys
import pygame

from maze import load_maze, find_position
from astar import a_star


CELL_SIZE = 40
MARGIN = 2
CONTROL_HEIGHT = 64


def draw_maze(screen, maze, path, path_index, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):
            x = c * (CELL_SIZE + MARGIN) + MARGIN
            y = r * (CELL_SIZE + MARGIN) + MARGIN

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if maze[r][c] == "#":
                color = (40, 40, 40)  # wall
            else:
                color = (220, 220, 220)  # empty

            pygame.draw.rect(screen, color, rect)

    # draw path up to path_index
    if path:
        # skip index 0 (start); draw from 1..path_index
        for (r, c) in path[1 : path_index + 1]:
            x = c * (CELL_SIZE + MARGIN) + MARGIN
            y = r * (CELL_SIZE + MARGIN) + MARGIN
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (255, 215, 0), rect)  # gold

    # draw start and goal
    sx = start[1] * (CELL_SIZE + MARGIN) + MARGIN
    sy = start[0] * (CELL_SIZE + MARGIN) + MARGIN
    gx = goal[1] * (CELL_SIZE + MARGIN) + MARGIN
    gy = goal[0] * (CELL_SIZE + MARGIN) + MARGIN

    pygame.draw.rect(screen, (50, 205, 50), pygame.Rect(sx, sy, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (220, 20, 60), pygame.Rect(gx, gy, CELL_SIZE, CELL_SIZE))


def draw_controls(screen, font, play, step_rect, play_rect, reset_rect):
    # background for control area
    w, h = screen.get_size()
    ctrl_rect = pygame.Rect(0, h - CONTROL_HEIGHT, w, CONTROL_HEIGHT)
    pygame.draw.rect(screen, (50, 50, 50), ctrl_rect)

    # draw buttons
    pygame.draw.rect(screen, (100, 100, 100), step_rect)
    pygame.draw.rect(screen, (100, 100, 100), play_rect)
    pygame.draw.rect(screen, (100, 100, 100), reset_rect)

    step_text = font.render('Step', True, (255, 255, 255))
    play_text = font.render('Pause' if play else 'Play', True, (255, 255, 255))
    reset_text = font.render('Reset', True, (255, 255, 255))

    screen.blit(step_text, (step_rect.x + 10, step_rect.y + 8))
    screen.blit(play_text, (play_rect.x + 10, play_rect.y + 8))
    screen.blit(reset_text, (reset_rect.x + 10, reset_rect.y + 8))


def main():
    filename = "sample_maze.txt"

    maze = load_maze(filename)

    if not maze:
        print("Failed to load maze from", filename)
        return

    start = find_position(maze, "S")
    goal = find_position(maze, "G")

    if start is None or goal is None:
        print("Maze must contain 'S' and 'G'")
        return

    path = a_star(maze, start, goal)

    rows = len(maze)
    cols = len(maze[0])

    width = cols * (CELL_SIZE + MARGIN) + MARGIN
    height = rows * (CELL_SIZE + MARGIN) + MARGIN + CONTROL_HEIGHT

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Solver Visualization")

    font = pygame.font.SysFont(None, 24)

    # button rects
    btn_w = 90
    btn_h = 40
    padding = 12
    step_rect = pygame.Rect(padding, height - CONTROL_HEIGHT + 10, btn_w, btn_h)
    play_rect = pygame.Rect(padding * 2 + btn_w, height - CONTROL_HEIGHT + 10, btn_w, btn_h)
    reset_rect = pygame.Rect(padding * 3 + btn_w * 2, height - CONTROL_HEIGHT + 10, btn_w, btn_h)

    clock = pygame.time.Clock()

    running = True
    playing = False
    path_index = 0
    fps_play = 6

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    playing = not playing
                elif event.key == pygame.K_RIGHT:
                    # step
                    if path:
                        path_index = min(path_index + 1, len(path) - 1)
                elif event.key == pygame.K_r:
                    # reset
                    path_index = 0
                    playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if step_rect.collidepoint(mx, my):
                    if path:
                        path_index = min(path_index + 1, len(path) - 1)
                elif play_rect.collidepoint(mx, my):
                    playing = not playing
                elif reset_rect.collidepoint(mx, my):
                    path_index = 0
                    playing = False

        if playing and path:
            # advance at controlled speed
            path_index = min(path_index + 1, len(path) - 1)

        screen.fill((30, 30, 30))

        # draw maze and current path progress
        draw_maze(screen, maze, path, path_index, start, goal)

        # draw controls area
        draw_controls(screen, font, playing, step_rect, play_rect, reset_rect)

        pygame.display.flip()

        clock.tick(fps_play if playing else 30)

    pygame.quit()


if __name__ == "__main__":
    main()
