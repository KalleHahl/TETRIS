import pygame
from src.game_modules.game_loop import Game
from src.tetris_logic.tetris import Tetris
from src.gui.renderer import Renderer
from src.game_modules.event_queue import EventQueue

WIDTH = 700
HEIGHT = 800


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    tetris = Tetris()
    renderer = Renderer(display, tetris)
    event_queue = EventQueue()
    loop = Game(display,tetris,renderer,event_queue)
    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
