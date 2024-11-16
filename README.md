# Tic-Tac-Toe Game with Tkinter

## Overview

This project is a simple **Tic-Tac-Toe** game implemented using Python's `tkinter` library. The game is designed for two players (Player X and Player O) who take turns to place their marks on a 3x3 grid. The game checks for a winner or a draw after each turn and allows resetting the board for a new game.

## Features

- **Interactive Gameplay**: Players can click on the buttons to make their move.
- **Win Detection**: Automatically checks for winning combinations after every move.
- **Draw Detection**: Declares a draw when the board is full, and no winning combination is present.
- **Reset Functionality**: Reset the board at any time to start a new game.
- **User-friendly Interface**: Built with `tkinter`, featuring labeled turns and notifications for wins or draws.

## Requirements

- Python 3.x
- `tkinter` library (pre-installed with most Python distributions)

## How to Run

1. Save the script as `tic_tac_toe.py`.
2. Run the script using Python:
   ```bash
   python tic_tac_toe.py
   ```
3. The game window will appear. Follow the instructions on the screen to play.

## Game Rules

1. The game is played on a 3x3 grid.
2. Players take turns marking a square with their symbol (X or O).
3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
4. If all squares are filled and no player has won, the game ends in a draw.

## Code Explanation

### Main Components

1. **GUI Setup**:
   - The game board is represented by 9 buttons arranged in a 3x3 grid.
   - A label indicates whose turn it is.
   - A "Reset Game" button allows restarting the game at any time.

2. **Game Logic**:
   - `check_win(player)`: Verifies if a player has a winning combination.
   - `handle_click(idx)`: Handles button clicks, updates the board, and checks for a win or draw.
   - `reset_board()`: Resets the game board and variables for a new game.

3. **Winning Combinations**:
   - Predefined winning combinations are stored in `winning_combos`.

### Highlights

- **Dynamic Player Turns**: The current player alternates after each valid move.
- **Visual Updates**: Button text and turn label update dynamically based on the game state.
- **Popup Notifications**: `messagebox` provides alerts for wins or draws.

## Folder Structure

```
tic_tac_toe/
│
└── tic_tac_toe.py   # Main script for the game
```
Enjoy playing Tic-Tac-Toe! 😊
