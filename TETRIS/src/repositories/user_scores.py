class UserScores:
    def __init__(self, connection):
        self._connection = connection

    def find_top_scores(self):
        cursor = self._connection.cursor()

        cursor.execute("select username, score from scores order by score limit 3")

        scores = cursor.fetchall()

        return scores

    def create_score(self, player, score):
        cursor = self._connection.cursor()

        cursor.execute('insert into scores (username, score) values (?,?)',
                       (player, score))
        
        self._connection.commit()

    