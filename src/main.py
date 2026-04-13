import pygame
import sys
import numpy as np
from path_planning.astar import astar

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
ROWS = WIDTH // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
LIGHT_BLUE = (173, 216, 230)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Navigation System")

clock = pygame.time.Clock()

grid = np.zeros((ROWS, ROWS))

start = (1, 1)
goal = (ROWS - 2, ROWS - 2)

# obstacles with gap
for i in range(5, 15):
    if i != 10:
        grid[10][i] = 1
    grid[i][15] = 1


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


def draw_cell(pos, color):
    r, c = pos
    pygame.draw.rect(
        screen,
        color,
        (c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
    )


def main():
    print("RUNNING PROGRAM")

    path = astar(grid, start, goal)
    print("PATH:", path)

    current_index = 0
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # obstacles
        for x in range(ROWS):
            for y in range(ROWS):
                if grid[x][y] == 1:
                    draw_cell((x, y), GRAY)

        # path
        for node in path:
            draw_cell(node, LIGHT_BLUE)

        # moving agent
        if len(path) > 0:
            if current_index < len(path):
                agent_pos = path[current_index]
                current_index += 1
            else:
                agent_pos = goal

            draw_cell(agent_pos, BLUE)

        draw_cell(start, GREEN)
        draw_cell(goal, RED)

        draw_grid()

        pygame.display.update()
        clock.tick(5)

    pygame.quit()
    sys.exit()


# 🔥 THIS LINE IS REQUIRED
if __name__ == "__main__":
    main()