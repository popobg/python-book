#! /usr/bin/env python3

import popo_tools, time, random

def randomize_row():
    row = []
    number_row = random.randrange(3, 5)
    for i in range(0, number_row):
        value = random.randrange(1, 11)
        row.append(value)
    return row

def display_board(board):
    for j in range(0, len(board)):
        print(f"row {j + 1}: ", end = "")
        for i in range(0, board[j]):
            print("| ", end = "")
        print(f" {board[j]}")

def remove_sticks(choice, board):
    return board - choice

def controlled_input(inp, board):
    while board[inp-1] == 0:
        inp = popo_tools.input_int("This row has no stick. Choose another one :\n> ")
    return inp

def player_turn(player, board):
    print(f"{player}: ")
    row_player_choice = popo_tools.input_int(player_prompt1, [1, len(board)])
    row_player_choice = controlled_input(row_player_choice, board)
    sticks_player_choice = popo_tools.input_int(player_prompt2, [1, board[row_player_choice -1]])
    board[row_player_choice-1] = remove_sticks(sticks_player_choice, board[row_player_choice -1])
    return board

def play_turn(player, board):
    board = player_turn(player, board)
    display_board(board)
    print()
    return board

def game_over(board):
    for i in board:
        if i == 0:
            continue
        else:
            return False
    return True

player_prompt1 = "Which row?"
player_prompt2 = "How many sticks?"

print("------ Nim game-----")
print("-------------------------")
print("There are 3 row of sticks.")
print("At their turn, the player have to choose a row and pull \nas many sticks as they want out of the row (at least one).")
print("The winner is the one taking the last stick out of the board.\n")
time = time.sleep(3)
player1 = input("First player: ")
player2 = input("Second player: ")
print()
row_val = randomize_row()
print("Here is the board :")
display_board(row_val)
print()

while True:
    row_val = play_turn(player1, row_val)
    if game_over(row_val):
        print(f"Congratulations {player1}, you win!")
        break
    row_val = play_turn(player2, row_val)
    if game_over(row_val):
        print(f"Congratulations {player2}, you win!")
        break