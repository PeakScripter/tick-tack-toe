import tkinter as tk
from tkinter import messagebox

def check_win(player):
    for combo in winning_combos:
        if all(board[i] == player for i in combo):
            return True
    return False


def handle_click(idx):
    global current_player, game_over
    if board[idx] == '' and not game_over:
        board[idx] = current_player
        buttons[idx].config(text=current_player)
        if check_win(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif '' not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            label.config(text=f"Player {current_player}'s turn")

def reset_board():
    for i in range(9):
        buttons[i].config(text='', state=tk.NORMAL)
    global board, current_player, game_over
    board = [''] * 9
    current_player = 'X'
    label.config(text="Player X's turn")
    game_over = False

window = tk.Tk()
window.title("Tic-Tac-Toe")
board = [''] * 9
buttons = []

for i in range(9):
    button = tk.Button(window, text='', width=10, height=4, command=lambda i=i: handle_click(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]

current_player = 'X'
label = tk.Label(window, text="Player X's turn", font=("Helvetica", 12))
label.grid(row=3, column=0, columnspan=3)
game_over = False
reset_button = tk.Button(window, text="Reset Game", command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3)
window.mainloop()
