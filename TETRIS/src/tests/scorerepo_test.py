import unittest
from src.database_connection import get_data_base_connection
from src.repositories.user_scores import UserScores


class TestScoreRepo(unittest.TestCase):
    def setUp(self):
        self.score_repo = UserScores(get_data_base_connection())
        self.score_repo.delete_all()

    def test_create_score(self):
        player = 'Kalle'
        score = 117
        self.score_repo.create_score(player, score)
        players = self.score_repo.find_top_scores()
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0][0], 'Kalle')
        self.assertEqual(players[0][1], 117)

    def test_top_3_correct_order(self):
        player1 = 'Kalle'
        player2 = 'Timo'
        player3 = 'Jankko'
        score1 = 300
        score2 = 200
        score3 = 100
        self.score_repo.create_score(player1, score1)
        self.score_repo.create_score(player2, score2)
        self.score_repo.create_score(player3, score3)
        players = self.score_repo.find_top_scores()
        self.assertEqual(players[0], ('Kalle', 300))
        self.assertEqual(players[1], ('Timo', 200))
        self.assertEqual(players[2], ('Jankko', 100))
        self.score_repo.delete_all()
