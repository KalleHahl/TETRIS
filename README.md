
<img src=https://github.com/KalleHahl/ot-harjoitustyo/blob/main/TETRIS/src/assets/TETRIS.png alt='pic'>

![CI Badge](https://github.com/KalleHahl/ot-harjoitustyo/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/KalleHahl/ot-harjoitustyo/branch/main/graph/badge.svg?token=D9XSGLPQI0)](https://codecov.io/gh/KalleHahl/ot-harjoitustyo)

Tetris game with leaderboards and a very 'unique' wall kick system.
## Installation:
Clone this repository to your desired directory

```bash
git clone https://github.com/KalleHahl/ot-harjoitustyo
```

Install dependencies


```bash
cd TETRIS
```

```bash
poetry install
```

Initialize database

```bash
poetry run invoke build
```

Start program

```bash
poetry run invoke start
```
## Command-line:
*Run these commands while in the TETRIS directory*

Initialize database:
```bash
poetry run invoke build
```

Start program:

```bash
poetry run invoke start
```

Unittests:

```bash
poetry run invoke test
```

Coverage:

```bash
poetry run coverage-report
```

Open coverage report HTML in browser:

```bash
poetry run coverage-show
```

Pylint:

```bash
poetry run invoke lint
```

## Documentation:
* [Project definition](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/definition.md)
* [Project architecture](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/architecture.md)
* [User guide](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/userguide.md)
* [Testing](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/testing.md)
* [Time-log](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/timelog.md)
* [Changelog](https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/changelog.md)
