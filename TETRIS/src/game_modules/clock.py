import pygame


class Clock:
    """Class for pygame clock

    Attributes:
        clock: pygame clock
    """
    def __init__(self):
        """Class constructor
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """

        Args:
            fps (int): updates clock
        """
        self._clock.tick(fps)
