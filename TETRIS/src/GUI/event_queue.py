import pygame

class EventQueue:
    
    def __init__(self):
        self.delay = pygame.USEREVENT + 1
        pygame.time.set_timer(self.delay, 500)

    def get(self):
        return pygame.event.get()