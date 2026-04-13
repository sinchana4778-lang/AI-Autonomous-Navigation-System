import pygame
import random

CELL_SIZE = 30

class GridEnvironment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self._generate_obstacles()

        pygame.init()
        self.screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
        pygame.display.set_caption("Autonomous Navigation Simulation")

    def _generate_obstacles(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < 0.2:
                    self.grid[i][j] = 1

    def draw(self, path=[], agent_pos=None, start=None, goal=None):
        self.screen.fill((255, 255, 255))

        for i in range(self.rows):
            for j in range(self.cols):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)

                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

        # Draw path
        for p in path:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                pygame.Rect(p[1] * CELL_SIZE, p[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        # Draw start
        if start:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                pygame.Rect(start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        # Draw goal
        if goal:
            pygame.draw.rect(
                self.screen,
                (0, 0, 255),
                pygame.Rect(goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        pygame.display.update()