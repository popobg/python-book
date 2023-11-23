#! /usr/bin/env python3

import popo_tools, random, time

def remove_sticks(choice, sticks_number):
    sticks_number = sticks_number - choice
    return sticks_number

def player_turn(sticks_number):
        upper_limit = 3 if sticks_number >= 3 else sticks_number
        player_move = popo_tools.input_int("It is your turn: ", [1, upper_limit])
        sticks_number = remove_sticks(player_move, sticks_number)
        return sticks_number

def computer_turn(sticks_number):
    computer_move = sticks_number % 4
    if computer_move == 0:
        computer_move = random.randrange(1, 4)
    print(f"The computer choose {computer_move} {make_stick_words(computer_move)}.")
    sticks_number = remove_sticks(computer_move, sticks_number)
    return sticks_number

def make_stick_words(sticks_number):
    return "stick" if sticks_number <= 1 else "sticks"

sticks_number = 21

print("There are 21 sticks. You can remove between 1 and 3 sticks at each round.")
print("The winner is the one that removes the last stick.")

while True:
    if sticks_number > 1:
        sticks_number = player_turn(sticks_number)
        print(f"{sticks_number} {make_stick_words(sticks_number)} remaining.")
        if sticks_number == 0:
            print("Congratulations, you win!")
            exit()
    else:
        print("It is your turn, you win.")
        exit()
    time.sleep(1)
    if sticks_number <= 3:
        print(f"The computer choose {sticks_number} {make_stick_words(sticks_number)}, you lose.")
        exit()
    else:
        sticks_number = computer_turn(sticks_number)
        print(f"{sticks_number} {make_stick_words(sticks_number)} remaining.")