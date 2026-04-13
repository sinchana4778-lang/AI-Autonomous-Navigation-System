from simulation.environment import GridEnvironment
from src.path_planning.astar import astar
import pygame

def main():
    pygame.init()

    env = GridEnvironment(rows=20, cols=20)

    start = None
    goal = None
    path = []
    agent_pos = None
    step_index = 0
    path_found = False

    running = True

    while running:
        env.draw(path[:step_index], agent_pos=agent_pos, start=start, goal=goal)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // 30
                col = x // 30

                if event.button == 1:  # Left click → Start
                    start = (row, col)
                    path = []
                    agent_pos = None
                    step_index = 0
                    path_found = False

                elif event.button == 3:  # Right click → Goal
                    goal = (row, col)
                    path = []
                    agent_pos = None
                    step_index = 0
                    path_found = False

            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[1]:  # Middle click → Draw obstacles
                    x, y = pygame.mouse.get_pos()
                    row = y // 30
                    col = x // 30
                    env.grid[row][col] = 1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset
                    start = None
                    goal = None
                    path = []
                    agent_pos = None
                    step_index = 0
                    path_found = False
                    env = GridEnvironment(rows=20, cols=20)

                elif event.key == pygame.K_s:  # Save screenshot
                    pygame.image.save(env.screen, "outputs/screenshot.png")
                    print("Screenshot saved!")

        # Compute path ONLY ONCE
        if start and goal and not path_found:
            path = astar(env.grid, start, goal)
            step_index = 0
            agent_pos = start
            path_found = True

        # Move step-by-step
        if path and step_index < len(path):
            agent_pos = path[step_index]
            step_index += 1
            pygame.time.delay(150)

        pygame.time.delay(30)

    pygame.quit()

if __name__ == "__main__":
    main()