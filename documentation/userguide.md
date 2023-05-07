# User guide
Download the source code for the latest [release](https://github.com/KalleHahl/ot-harjoitustyo/releases/tag/Week6) from the zip file below the Assets-text.
## Start:
To start the program, follow these steps:

```cd TETRIS```

```poetry install```

Initialize database:

```poetry run invoke build```

Now you can run the program by typing:

```poetry run invoke start```

## Keyboard actions:
- At the start, press space to exit menu and start playing
- Pressing the escape after the menu pauses the game, unpause by pressing escape again
- Move the piece with arrow keys
- Rotate piece by pressing arrow key up
- Pressing space immediately drops piece to the bottom
- Exit the game by clicking the x button in the corner of the screen with cursor
