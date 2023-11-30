#! /usr/bin/env python3

# redo the ping_pong game with a mutual recursion between ping() and pong().

import random

def play_ping_turn(prob_ping = 0.5, prob_pong = 0.5):
    prob_success = random.random()
    if prob_success < prob_ping:
        winner = play_pong_turn(prob_pong, prob_ping)
        return winner
    else:
        return 1

def play_pong_turn(prob_pong = 0.5, prob_ping = 0.5):
    prob_success = random.random()
    if prob_success < prob_pong:
        winner = play_ping_turn(prob_ping, prob_pong)
        return winner
    else:
        return 0

def game_over(win_count):
    """return the boolean True if a player won 11 times
    and has a 2-point margin with his adversary"""
    if win_count[0] >= 11 and win_count[1] <= (win_count[0] - 2) or win_count[1] >= 11 and win_count[0] <= (win_count[1] - 2):
        return True
    return False

def print_set_winner(winner, win_count):
    if winner == 0:
        print("ping won this set.")
        win_count[0] += 1
    else:
        print("pong won this set.")
        win_count[1] += 1
    return win_count

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

win_count = [0, 0]
turn = 0

while not game_over(win_count):
    if turn % 2 == 0 :
        turn += 1
        winner = play_ping_turn()
        print_set_winner(winner, win_count)

    else :
        turn += 1
        winner = play_pong_turn()
        print_set_winner(winner, win_count)

print("-----------")
print_winner(win_count)