import pygame


class EventQueue:

    def __init__(self):
        self.speed = 750
        self.delay = pygame.constants.USEREVENT + 1
        pygame.time.set_timer(self.delay, self.speed)
        self.move_down_fast = pygame.constants.USEREVENT + 2
        pygame.time.set_timer(self.move_down_fast, 30)

    def get(self):
        return pygame.event.get()
    
    def set_speed(self):
        self.speed = self.speed // 2
        pygame.time.set_timer(self.delay, self.speed)
