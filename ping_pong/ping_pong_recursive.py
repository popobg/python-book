#! /usr/bin/env python3

import random

def ping(prob):
    """return the boolean True if the player succed to return the ball"""
    prob_success = random.random()
    return prob_success < prob

def pong(prob):
    return ping(prob)

def game_over(win_count):
    """return the boolean True if a player won 11 times
    and has a 2-point margin with his adversary"""
    if win_count[0] >= 11 and win_count[1] <= (win_count[0] - 2) or win_count[1] >= 11 and win_count[0] <= (win_count[1] - 2):
        return True
    return False

def ping_first(return_ball, win_count, last_winner):
    while return_ball:
        return_ball = ping(0.7)
        if return_ball:
            return_ball = pong(0.3)
            if not return_ball:
                print("ping won this set.")
                win_count[0] += 1
            else:
                continue
        else:
            print("pong won this set.")
            win_count[1] += 1
            last_winner = 1
    return return_ball, win_count, last_winner

def pong_first(return_ball, win_count, last_winner):
    while return_ball:
        return_ball = pong(0.3)
        if return_ball:
            return_ball = ping(0.7)
            if not return_ball:
                print("pong won this set.")
                win_count[1] += 1
                last_winner = 1
            else:
                continue
        else:
            print("ping won this set.")
            win_count[0] += 1
    return return_ball, win_count, last_winner

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
    winner = determine_overall_winner(win_count)
    if winner == "ping":
        print(f"Ping won {win_count[0]} vs {win_count[1]}.")
        return
    if winner == "pong":
        print(f"Pong won {win_count[1]} vs {win_count[0]}.")
        return
    print(f"It's a tie : {win_count[0]} = {win_count[1]}.")

return_ball = True
win_count = [0, 0]
last_winner = 0

return_ball, win_count, last_winner = ping_first(return_ball, win_count, last_winner)

while not game_over(win_count):
    return_ball = True
    if last_winner == 0:
        return_ball, win_count, last_winner = ping_first(return_ball, win_count, last_winner)

    else:
        return_ball, win_count, last_winner = pong_first(return_ball, win_count, last_winner)

print("-----------")
print_winner(win_count)