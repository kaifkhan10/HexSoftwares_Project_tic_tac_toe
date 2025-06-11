import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe - Player vs Computer")

# Game state
board = ['' for _ in range(9)]
buttons = []

# Players
PLAYER = 'X'
COMPUTER = 'O'

# Winning combinations
win_combinations = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner(symbol):
    for combo in win_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False

def is_draw():
    return all(cell in ['X', 'O'] for cell in board)

def disable_all_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def computer_move():
    # Block player if needed
    for i in range(9):
        if board[i] == '':
            board[i] = PLAYER
            if check_winner(PLAYER):
                board[i] = COMPUTER
                buttons[i].config(text=COMPUTER, state=tk.DISABLED)
                return
            board[i] = ''

    # Pick a random empty cell
    empty_cells = [i for i in range(9) if board[i] == '']
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = COMPUTER
        buttons[move].config(text=COMPUTER, state=tk.DISABLED)

        if check_winner(COMPUTER):
            messagebox.showinfo("Game Over", "💻 Computer wins!")
            disable_all_buttons()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_all_buttons()

def on_click(index):
    if board[index] == '':
        board[index] = PLAYER
        buttons[index].config(text=PLAYER, state=tk.DISABLED)

        if check_winner(PLAYER):
            messagebox.showinfo("Game Over", "🎉 You win!")
            disable_all_buttons()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_all_buttons()
        else:
            root.after(500, computer_move)

def reset_game():
    global board
    board = ['' for _ in range(9)]
    for btn in buttons:
        btn.config(text='', state=tk.NORMAL)

# Create buttons in a 3x3 grid
for i in range(9):
    btn = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Add reset button
reset_btn = tk.Button(root, text="Reset Game", font=('Arial', 12), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Run the game
root.mainloop()