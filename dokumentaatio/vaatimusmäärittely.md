# Project definition
## App:
[Tetris](https://en.wikipedia.org/wiki/Tetris)-game, where you can save score into a database. You can see the top-10 highscores in a ```leaderboards```-table.

## GUI:
The games GUI is coded using Pythons ```pygame```-library. You can also see the ```leaderboards```-table in the same window.

## Tetris:
* The game randomizes a block (I, J, L, O, S, T, Z) that starts moving down the screen
* The block is moved to the sides using the arrow keys
* Block rotation is done by pressing the arrow key up
* A block cannot cross the screen from any direction
* A block stops on the bottom or if it hits another block
* A full row is cleared
* The game ends when a block hits the top edge
* At the end of the game, the result is stored in the database under the name chosen by the user

## Further improvement:
* The ability to log in and register
