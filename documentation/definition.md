# Project definition
## App:
[Tetris](https://en.wikipedia.org/wiki/Tetris)-game, where you can save scores into a database. You can see the top-3 highscores in a Highscores-table in the starting menu.

## GUI:
The games GUI is coded using Pythons ```pygame```-library. The GUI has a menu, game, pause, game over and score saved state.

<img src=https://github.com/KalleHahl/ot-harjoitustyo/blob/main/documentation/pictures/UI.gif alt="gif" width="600" height="700" title="untitled">

## Tetris:
- The game randomizes a piece (I, J, L, O, S, T, Z) which starts moving down the screen
- The piece is moved to the sides using the arrow keys &#8592; and &#8594;
- Piece rotation is done by pressing the arrow key &#8593;
- A piece can be soft dropped by pressing arrow key &#8595;
- A piece can be hard dropped by pressing ```space```
- A piece cannot cross the screen from any direction
- A piece stops on the bottom or if it hits another piece
- A full row is cleared
- The game ends when a piece hits the top edge
- Speed is increased every ten line clears
- A scoring system is in use, which resembles the [original Nintendo scoring system](https://tetris.wiki/Scoring#Original_Nintendo_scoring_system)
- A very crude wallkick system is enabled
- At the end of the game, the result is stored in the database under the name chosen by the user
- Database is implemented using sqlite3
## Further improvement:
* The ability to log in and register
* The ability to hold a piece
