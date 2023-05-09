# Architecture
## Packaging & Classes
![Picture](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/pictures/package_diagram.png)

## Storing scores in database
[UserScores](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/TETRIS/src/repositories/user_scores.py) is responsible for storing scores into the database configured in the .env file. The project uses a SQLite-database and scores are stored in the ```scores```-table, which has entries username and score.

## Sequences
### Storing score:
![img](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/pictures/score_save_diagram.png)
