import pygame
from game_modules.game_loop import Game

WIDTH = 400
HEIGHT = 800


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    tetris = Game(display)
    pygame.init()
    tetris.start()


if __name__ == "__main__":
    main()
