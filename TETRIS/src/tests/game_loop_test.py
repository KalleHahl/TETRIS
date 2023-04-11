import unittest
import pygame
from src.tetris_logic.tetris import Tetris
from src.game_modules.game_loop import Game


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris()
