# Testing documentation
The project has been tested using automated unittests with pythons unittest module and manually testing the GUI.

## Unittests:

### Tetris-logic:
The two classes responsible for the gameplay logic (```Tetris``` & ```Piece```) are thoroughly tested with [TetrisTest](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/TETRIS/src/tests/tetris_test.py) and [TestPiece](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/TETRIS/src/tests/piece_test.py) test classes. Testing with these classes focuses on gameplay aspects such as correct handling when piece is out of bounds and checking that level, score and lines cleared are tracked. Each test is named according to what is being tested, so I will not be going over every test here.

### Score-repository:
Testing the class responsible for database related actions (```UserScores```) is tested with [TestScoreRepo](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/TETRIS/src/tests/scorerepo_test.py) test class. The tests use a separate database file configured in the .env.test-file. The test class tests only that new score can be created and that top 3 scores are fetched from the database in the correct order.

### Coverage:

![CI Badge](https://github.com/KalleHahl/ot-harjoitustyo/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/KalleHahl/ot-harjoitustyo/branch/main/graph/badge.svg?token=D9XSGLPQI0)](https://codecov.io/gh/KalleHahl/ot-harjoitustyo)

![image]()

All files that didn't need automated testing have been omitted in the .coveragerc file

## Start up & GUI:

Manual testing has been done for startup and GUI related stuff. The project has been installed and played according to the instructions found in the [User guide](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/userguide.md) and the database has been re-initialized multiple times and no issues have been detected yet. Different configurations for database filenames have also been tested.

## Quality issues:
* Gameloop is not tested
