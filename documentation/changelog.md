# Changelog
## Week 3
* Refactored the code, created separate classes for gameloop, rendering and events
* Added pylint,autopep8,pytest,invoke
* Added tests for Piece and Tetris classes
* Added necessary tasks to tasks.py
* The game now has movement, collision with edges and other pieces, full lines get cleared and pieces can be rotated
* Added a deque that acts as a board to store locations of pieces in the tetris board
* Added a pause feature by pressing space
* Documentation
## Week 4
* Game now ends if pieces reach the top
* Game can be restarted when it ends
* Crude version of main menu
* Screen is now wider for future additions, board stayed the same size
* Added class or clock
* Added rendering of next piece
* Added current score rendering
## Week 5
* Crude version of wallkicks, may need to change it a bit
* Added a ghost piece which shows where the piece is going to land
* Game speed now increases every 10 points
## Week 6
* Added docstrings and userguide
## Week 7
* Added blur screen when paused and game over
* Added input box where player name is written
* Added new background and improved UI
* Added jump down method to immediately drop piece
* Added database to keep track of scores
* Added method to return top 3 scores from database
* Top 3 scores are now rendered on menu screen
* Changed scoring system to resemble the original Nintendo scoring system
* Added pictures for buttons, UI now prettier
