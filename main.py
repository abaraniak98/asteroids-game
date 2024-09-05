# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        delta_time = fps_clock.tick(60)
        dt = delta_time/1000

if __name__ == "__main__":
    main()
