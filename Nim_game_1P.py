#! /usr/bin/env python3

import popo_tools, time, random

def create_random_board():
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

def player_turn(board):
    player_row_choice = popo_tools.input_int(player_prompt1, [1, len(board)])
    player_row_choice = controlled_input(player_row_choice, board)
    player_sticks_choice = popo_tools.input_int(player_prompt2, [1, board[player_row_choice - 1]])
    board[player_row_choice - 1] = remove_sticks(player_sticks_choice, board[player_row_choice - 1])
    return board

def parity(board):
    parity = 0
    for i in range(len(board)):
        parity = parity ^ board[i]
    return parity

def calculate_null_parity(board):
    new_board = board.copy()
    for i in range(0, len(board)):
        for j in range(1, board[i] + 1):
            new_board[i] = board[i] - j
            if parity(new_board) == 0:
                return i, j
            else:
                continue

def make_stick_words(sticks_number):
    return "stick" if sticks_number == 1 else "sticks"

def computer_turn(board):
    if parity(board) == 0:
        computer_row_choice = random.randrange(len(board))
        while board[computer_row_choice] == 0:
            computer_row_choice = random.randrange(len(board))

        computer_sticks_choice = random.randrange(1, board[computer_row_choice] + 1)
    else:
        computer_row_choice, computer_sticks_choice = calculate_null_parity(board)

    print(f"Computer removed {computer_sticks_choice} {make_stick_words(computer_sticks_choice)} from row {computer_row_choice + 1}.")

    board[computer_row_choice] = remove_sticks(computer_sticks_choice, board[computer_row_choice])
    return board

def game_over(board):
    for i in board:
        if i != 0:
            return False
    return True

player_prompt1 = "Which row?"
player_prompt2 = "How many sticks?"

print("------ Nim game-----")
print("-------------------------")
print("There are 3 row of sticks.")
print("At their turn, the player have to choose a row and pull \nas many sticks as they want out of the row (at least one).")
print("The winner is the one taking the last stick out of the board.\n")
board = create_random_board()
print("Here is the board :")
display_board(board)
print()

while True:
    print("It is your turn.")
    board = player_turn(board)
    display_board(board)
    print()
    if game_over(board):
        print(f"Congratulations, you win!")
        break
    time1 = time.sleep(1)
    print("It is the computer turn.")
    board = computer_turn(board)
    display_board(board)
    time2 = time.sleep(2)
    print()
    if game_over(board):
        print(f"Sorry, you lose")
        break