# User guide
Download the source code for the final [release](https://github.com/KalleHahl/ot-harjoitustyo/releases/tag/Final) from the zip file below the Assets-text.
## Configuration:
Database names can be configured in the .env-file found in the *TETRIS*-directory. The files will be automatically created in the *data*-directory if they don't exist.
## Start:
Open the *TETRIS*-directory and install dependencies:

```bash
cd TETRIS
```

```bash
poetry install
```

Initialize database:

```bash
poetry run invoke build
```

Now you can run the program by typing:

```bash
poetry run invoke start
```

## Keyboard actions:
- At the start, press ```Space``` to exit menu and start playing
- Pressing ```Escape``` after the menu pauses the game, unpause by pressing ```Escape``` again
- Move the piece sideways by pressing arrow key &#8592; or &#8594;
- Rotate piece by pressing arrow key &#8593;
- Soft drop the piece by pressing arrow key &#8595;
- Hard drop the piece by pressing ```Space```
- Exit the game by clicking the x button in the corner of the screen with cursor

## Saving a score:
- Save your score by typing your name and pressing ```Enter```

<img src=https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/pictures/Game_over.png alt='pic' width='600' height='700'>
