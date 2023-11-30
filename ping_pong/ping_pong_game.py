#! /usr/bin/env python3

import random

def success(probability = 0.5):
    """return the boolean True if the player succed to return the ball"""
    # random.random() generates a float number between 0 and 1
    proba_success = random.random()
    return proba_success < probability

def game_over(win_count):
    """return the boolean True if a player won 11 times
    and has a 2-point margin with his adversary"""
    if win_count[0] >= 11 and win_count[1] <= (win_count[0] - 2) or win_count[1] >= 11 and win_count[0] <= (win_count[1] - 2):
        return True
    return False

def print_set_winner(rally, win_count, switch_turn):
    """print the winner of this set."""
    if rally % 2 == 0 and switch_turn == True:
        win_count[1] += 1
        print("Pong won this set.")
        return win_count
    if rally % 2 == 1 and switch_turn == True:
        win_count[0] += 1
        print("Ping won this set.")
        return win_count
    if rally % 2 == 0 and switch_turn == False:
        win_count[0] += 1
        print("Ping won this set.")
        return win_count
    else:
        win_count[1] += 1
        print("Pong won this set.")
        return win_count

def switch_turn(current_player):
    """switch the boolean to change the first player
    True for ping, False for pong"""
    return not current_player

def determine_overall_winner(win_count):
    """determine the winner of the game."""
    if win_count[0] > win_count[1]:
        return "Ping"
    if win_count[0] < win_count[1]:
        return "Pong"

def print_winner(win_count):
    """print the winner of the game."""
    win_count_sorted = sorted(win_count)
    print(f"{determine_overall_winner(win_count)} won {win_count_sorted[1]} vs {win_count_sorted[0]}")

rally = 0
round = 0
first_player = True
return_ball = True
win_count = [0, 0]

while not game_over(win_count):
    while return_ball:
        rally += 1
        return_ball = success(0.7)
    # switch player every two rounds
    if round != 0 and round % 2 == 0 :
        first_player = switch_turn(first_player)
    win_count = print_set_winner(rally, win_count, first_player)
    rally = 0
    return_ball = True
    round += 1

print_winner(win_count)