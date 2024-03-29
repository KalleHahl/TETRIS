import pygame


class EventQueue:
    """Class for handling events

    Attributes:
        speed: game speed for delay timer
        delay: userevent for moving piece down periodically
        move_down_fast: user event for moving piece down faster
    """

    def __init__(self):
        """Class constructor
        """
        self.speed = 1000
        self.delay = pygame.constants.USEREVENT + 1
        pygame.time.set_timer(self.delay, self.speed)
        self.move_down_fast = pygame.constants.USEREVENT + 2
        pygame.time.set_timer(self.move_down_fast, 30)

    def get(self):
        """Method for fetching events

        Returns:
            function: returns pygame events
        """
        return pygame.event.get()

    def set_speed(self, level):
        """Method for changing game speed

        Args:
            level (int): current level in tetris game
        """
        self.speed = 1000 // (level + 1)
        pygame.time.set_timer(self.delay, self.speed)
