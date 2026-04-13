import pygame
import time

class Navigator:
    def __init__(self, env, path):
        self.env = env
        self.path = path

    def run(self):
        for pos in self.path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.env.draw(self.path, pos)
            time.sleep(0.1)