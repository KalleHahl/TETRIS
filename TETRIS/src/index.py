import pygame
from src.game_modules.game_loop import Game
from src.tetris_logic.tetris import Tetris
from src.gui.renderer import Renderer
from src.game_modules.event_queue import EventQueue
from src.game_modules.clock import Clock
from src.settings import WIDTH, HEIGHT
from src.repositories.user_scores import UserScores
from src.database_connection import get_data_base_connection


def main():
    """Main function which starts program when called
    """
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    tetris = Tetris()
    renderer = Renderer(display, tetris)
    event_queue = EventQueue()
    clock = Clock()
    score_repo = UserScores(get_data_base_connection())
    loop = Game(display, tetris, renderer, event_queue, clock, score_repo)
    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
