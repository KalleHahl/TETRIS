class UserScores:
    """Repository class for saving user scores to database
    """

    def __init__(self, connection):
        """Class constructor

        Args:
            connection (sqlite connection): connection to database
        """
        self._connection = connection

    def find_top_scores(self):
        """Method for finding top 3 scores from scores table

        Returns:
            list: list of tuples with username and score
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select username, score from scores order by score desc limit 3")

        scores = cursor.fetchall()

        return [(score["username"], score["score"]) for score in scores]

    def create_score(self, player, score):
        """Method for adding a score to database

        Args:
            player (string): player name
            score (int): player score
        """
        cursor = self._connection.cursor()

        cursor.execute('insert into scores (username, score) values (?,?)',
                       (player, score))

        self._connection.commit()

    def delete_all(self):
        """Deletes all scores
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from scores")

        self._connection.commit()