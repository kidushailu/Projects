import tkinter as tk
from tkinter import messagebox

game = [[' ' for _ in range(3)]for _ in range(3)]
player = 'X'
X_count = 0
O_count = 0


# FUNCTION FOR DETERMINING WHAT HAPPENS WHEN A BOX IS SELECTED
def button_click(row, col):
    global player

    if game[row][col] == ' ':
        game[row][col] = player
        buttons[row][col].config(text=player, fg='red') if player == 'X' else buttons[row][col].config(text=player, fg='blue')

        if check_winner(player):
            messagebox.showinfo('Tic Tac Toe', f'Player {player} wins the round!')
            scoreboard()
            clear_board()
            if X_count == 5:
                messagebox.showinfo('Game Over', f'Player X wins!\nCongrats!')
                scoreboard()
                reset_scoreboard()
            elif O_count == 5:
                messagebox.showinfo('Game Over', f'Player O wins!\nCongrats!')
                scoreboard()
                reset_scoreboard()
        elif all([cell != ' ' for row in game for cell in row]):
            messagebox.showinfo('Tic Tac Toe', "IT'S A TIE!\nLooks like you're evenly matched!")
            clear_board()
        else:
            player = 'O' if player == 'X' else 'X'
            turn.config(text=f"{player}'s turn", font=('Arial', 18))
    else:
        messagebox.showerror('TicTacToe', 'Hey! This box has already been selected.\nPlease select an empty box...')


# FUNCTION TO DETERMINE WHO WINS
def check_winner(player):
    for row in game:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if [game[row][col] for row in range(3)].count(player) == 3:
            return True

    if game[0][0] == game[1][1] == game[2][2] == player:
        return True
    if game[0][2] == game[1][1] == game[2][0] == player:
        return True
    return False


# FUNCTION TO CLEAR ALL X'S AND O'S
def clear_board():
    global game, player
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', bg='white')
    turn.config(text=f"X goes first", font=('Arial', 18))


# FUNCTION TO KEEP TRACK OF EACH PLAYER'S SCORE
def scoreboard():
    global X_count, O_count, player

    if player == 'X':
        X_count += 1
        X_score.config(text=f'Player {player}\n {X_count}')
    else:
        O_count += 1
        O_score.config(text=f'Player {player}\n {O_count}')


# FUNCTION TO CLEAR THE SCOREBOARD AND START OVER
def reset_scoreboard():
    global X_count, O_count
    X_count = 0
    O_count = 0
    X_score.config(text=f'Player X\n {X_count}')
    O_score.config(text=f'Player O\n {O_count}')
    clear_board()


window = tk.Tk()
bg_color = 'gray'
fg_color = 'white'
window.config(bg=bg_color)
window.title('Tic Tac Toe')
turn = tk.Label(text=f"X goes first", font=('Arial', 18), bg=bg_color, fg=fg_color)
turn.grid(row=3, column=1, columnspan=3)
X_score = tk.Label(text=f'Player X\n{X_count}', font=('Arial', 10), bg='dark gray', fg=fg_color)
O_score = tk.Label(text=f'Player O\n{O_count}', font=('Arial', 10), bg='dark gray', fg=fg_color)
X_score.grid(row=2, column=1, columnspan=2)
O_score.grid(row=2, column=2, columnspan=2)
to_win = tk.Label(text='First player to win 5 rounds wins!', font=('Arial', 15), bg=bg_color, fg=fg_color)
to_win.grid(row=1, column=1, columnspan=3)
reset = tk.Button(window, text='Reset Game', font=('Arial', 10), bg='red', fg='white', command=lambda: reset_scoreboard())
reset.grid(row=3, column=3)
clear = tk.Button(window, text='Clear Board', font=('Arial', 10), bg='red', fg='white', command=lambda: clear_board())
clear.grid(row=3, column=1)
tk.Label(text='    ', bg=bg_color).grid(row=0, column=0)
tk.Label(text='    ', bg=bg_color).grid(row=0, column=4)
tk.Label(text='   ', bg=bg_color).grid(row=7, column=0)

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(window, text=' ', font=('Arial', 30), width=5, height=2, bg='white',
                                     command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row+4, column=col+1)
window.mainloop()

