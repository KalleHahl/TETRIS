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