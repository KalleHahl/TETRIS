
# Tetris
![CI Badge](https://github.com/KalleHahl/ot-harjoitustyo/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/KalleHahl/ot-harjoitustyo/branch/main/graph/badge.svg?token=D9XSGLPQI0)](https://codecov.io/gh/KalleHahl/ot-harjoitustyo)

Tetris game with leaderboards and a very 'unique' wall kick system.
## Installation:
Clone this repository to your desired directory

```git clone https://github.com/KalleHahl/ot-harjoitustyo```

Install dependencies


```cd TETRIS```

```poetry install```

Initialize database

```poetry run invoke build```

Start program

```poetry run invoke start```
## Command-line:
*Run these commands while in the TETRIS directory*

Start program:

```poetry run invoke start```

Unittests:

```poetry run invoke test```

Coverage:

```poetry run coverage-report```

Open coverage report HTML in browser:

```poetry run coverage-show```

Pylint:

```poetry run invoke lint```

## Documentation:
* [User guide](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/userguide.md)
* [Project definition](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/definition.md)
* [Time-log](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/timelog.md)
* [Changelog](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/changelog.md)
* [Project architecture](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/architecture.md)
