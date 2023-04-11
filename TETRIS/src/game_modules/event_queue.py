import pygame


class EventQueue:

    def __init__(self):
        self.delay = pygame.USEREVENT + 1
        pygame.time.set_timer(self.delay, 750)
        self.move_down_fast = pygame.USEREVENT + 2
        pygame.time.set_timer(self.move_down_fast, 30)

    def get(self):
        return pygame.event.get()
