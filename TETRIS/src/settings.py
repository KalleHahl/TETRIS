import pygame

WIDTH = 700
HEIGHT = 800

"""Dimensions
"""
BOARD_WIDTH = 400
BOARD_HEIGHT = HEIGHT
BLOCK = 40


LINE = (128, 128, 128)

"""Necessary images
"""
BACKGROUND_IMG = pygame.image.load("src/assets/aurora.jpg")
TETRIS_LOGO = pygame.image.load("src/assets/TETRIS.png")
TETRIS_LOGO_SCALED = pygame.transform.scale(TETRIS_LOGO, (600, 140))
GAMEOVER_IMG = pygame.image.load("src/assets/GAMEOVER.png")
NEXT_PIECE_IMG = pygame.image.load("src/assets/NEXT1.png")
SCORE_IMG = pygame.image.load("src/assets/SCORE1.png")
START_IMG = pygame.image.load("src/assets/START.png")
RESUME_IMG = pygame.image.load("src/assets/RESUME.png")
SCORE_SAVED_IMG = pygame.image.load("src/assets/SCORE_SAVED.png")
HIGHSCORES_IMG = pygame.image.load("src/assets/HIGHSCORES.png")
LEVEL_IMG = pygame.image.load("src/assets/level.png")
LINES_IMG = pygame.image.load("src/assets/lines.png")


"""Piece colors
"""
colors = {
    'I': (0, 204, 204),
    'T': (178, 58, 238),
    'O': (238, 238, 0),
    'L': (255, 165, 0),
    'J': (0, 0, 190),
    'S': (117, 204, 32),
    'Z': (255, 48, 48)
}

wall_kick_offsets = {
    **dict.fromkeys(['T', 'L', 'J', 'S', 'Z'],
                    [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                     [(0, 0), (40, 0), (40, -40), (0, 40), (40, 80)],
                     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                     [(0, 0), (-40, 0), (-40, -40), (0, 40), (-40, 80)]]),
    'I': [[(0, 0), (-40, 0), (80, 0), (0, 0), (80, 0)],
          [(-40, 0), (0, 0), (0, 0), (0, 80), (0, -80)],
          [(-40, 40), (40, 0), (-80, 0), (40, 0), (0, 0)],
          [(0, 40), (0, 0), (0, 0), (0, -40), (0, 40)]],
    'O': [[(0, 0)]]
}

"""All pieces and their rotations
"""
pieces = {
    'T': [[(0, 0), (-1, 0), (1, 0), (0, -1)],
          [(0, 0), (0, -1), (0, 1), (1, 0)],
          [(0, 0), (-1, 0), (1, 0), (0, 1)],
          [(0, 0), (-1, 0), (0, -1), (0, 1)]],
    'I': [[(0, 0), (1, 0), (-1, 0), (2, 0)],
          [(0, 0), (0, 1), (0, -1), (0, 2)],
          [(0, 0), (-2, 0), (-1, 0), (1, 0)],
          [(0, 0), (0, 1), (0, -2), (0, -1)]],
    'O': [[(0, 0), (0, -1), (1, 0), (1, -1)]],
    'L': [[(1, -1), (1, 0), (0, 0), (-1, 0)],
          [(1, 1), (0, 1), (0, 0), (0, -1)],
          [(-1, 1), (-1, 0), (0, 0), (1, 0)],
          [(-1, -1), (0, -1), (0, 0), (0, 1)]],
    'J': [[(-1, -1), (-1, 0), (0, 0), (1, 0)],
          [(0, -1), (0, 0), (0, 1), (1, -1)],
          [(-1, 0), (0, 0), (1, 0), (1, 1)],
          [(-1, 1), (0, 1), (0, 0), (0, -1)]],
    'S': [[(0, 0), (0, -1), (1, -1), (-1, 0)],
          [(0, 0), (0, -1), (1, 0), (1, 1)],
          [(0, 0), (1, 0), (0, 1), (-1, 1)],
          [(0, 0), (0, 1), (-1, 0), (-1, -1)]],
    'Z': [[(0, 0), (0, -1), (-1, -1), (1, 0)],
          [(0, 0), (1, 0), (1, -1), (0, 1)],
          [(0, 0), (-1, 0), (0, 1), (1, 1)],
          [(0, 0), (-1, 0), (-1, 1), (0, -1)]]
}
