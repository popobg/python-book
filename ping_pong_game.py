#! /usr/bin/env python3

import random

def success(probability = 0.5):
    """return the boolean True if the player succed to return the ball"""
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
    if not switch_turn:
        if rally % 2 == 0:
            win_count[0] += 1
            print("Ping won this set.")
            return win_count
        else:
            win_count[1] += 1
            print("Pong won this set.")
            return win_count
    if switch_turn:
        if rally % 2 == 0:
            win_count[1] += 1
            print("Pong won this set.")
            return win_count
        else:
            win_count[0] += 1
            print("Ping won this set.")
            return win_count

def switch_turn(turn, previous_roll):
    """return the boolean True to switch first player if the player started twice."""
    if previous_roll + 2 == turn:
        return True
    return False

def determine_overall_winner(win_count):
    """determine the winner of the game."""
    if win_count[0] > win_count[1]:
        return "ping"
    if win_count[0] < win_count[1]:
        return "pong"
    return "tie"

# should I rather make a print_winner_and_exit() function?
def print_winner(win_count):
    """print the winner of the game."""
    if determine_overall_winner(win_count) == "ping":
        print(f"Ping won {win_count[0]} vs {win_count[1]}.")
        return
    if determine_overall_winner(win_count) == "pong":
        print(f"Pong won {win_count[1]} vs {win_count[0]}.")
        return
    print("It's a tie.")

rally = 0
turn = 0
previous_turn = 0
return_ball = True
win_count = [0, 0]

while not game_over(win_count):
    turn += 1
    while return_ball:
        rally += 1
        return_ball = success(0.7)
    whose_turn = switch_turn(turn, previous_turn)
    win_count = print_set_winner(rally, win_count, whose_turn)
    rally = 0
    return_ball = True


print_winner(win_count)