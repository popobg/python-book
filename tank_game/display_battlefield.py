#! /usr/bin/env python3

import os, time

# objectif 1 : afficher dans le terminal une image du terrain avec le canon, la cible et le boulet suivant la position (x, y) du boulet
# objectif 2 : ajouter un calcul simple de la trajectoire du boulet et de l'endroit où il tombe
# objectif 3 : ajouter l'affichage / ajouter l'input utilisateur

# CLASSES

class Sprite:
    def __init__(self, x, y, sprite):
        self.__x = x
        self.__y = y
        self.__sprite = sprite

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_sprite(self):
        return self.__sprite

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def set_sprite(self, sprite):
        self.__sprite = sprite

class Cannon(Sprite):
    def __init__(self, x, y):
        # call the method init of the superclass Sprite to initialize the attributes of the subclass Cannon
        Sprite.__init__(self, x, y, "/")

class Target(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y, "\\")

class Cannonball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y, "o")

    def update_position(self, dx, dy):
        """update the position of the moving object by adding the acceleration vectors dx and dy"""
        x = Sprite.get_x(self)
        x += dx
        Sprite.set_x(self, round(x))
        y = Sprite.get_y(self)
        y += dy
        Sprite.set_y(self, round(y))

class Impact(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y, "X")

class Display:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__sprites = []
        self.__init_display__()

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def add_sprite(self, sprite: Sprite):
        self.__sprites.append(sprite)

    def remove_sprite(self, sprite: Sprite):
        self.__sprites.pop()

    def __init_display__(self):
        """create a list of lists defining the range of the field"""
        self.__field = []
        for i in range(self.__height):
            self.__field.append([" "] * self.__width)
        return self

    def draw_battlefield(self):
        """draw battlefield by printing the field and sprites on the terminal"""
        self.__init_display__()
        # replace the blank by the objects's sprite at the right position in the field
        for sprite in self.__sprites:
            self.__field[sprite.get_y()][sprite.get_x()] = sprite.get_sprite()
        for line in self.__field[::-1]:
            print("-", end = "")
            print("".join(line))
        print("", "|" * self.__width)

# FUNCTIONS

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait():
    time.sleep(1)

def calculate_moving_vectors(d: Display):
    dy = 0.1 * d.get_height()
    dx = 0.1 * d.get_width()
    return dx, dy

def applicate_friction(dy, initial_dy, dx, initial_dx):
    """update dx and dy to apply deceleration on the ball"""
    dy = dy - initial_dy
    dx = dx * 0.8
    return dy, dx

def update_display(d: Display):
    clear()
    d.draw_battlefield()
    wait()

def ball_out_of_field(s: Sprite, d: Display):
    """return True if the ball is out of the range of the field or on the ground
    otherwise return False"""
    if s.get_y() <= 0:
        return True
    if s.get_y() > d.get_height() or s.get_x() > d.get_width():
        return True
    return False

def determine_x(s: Sprite, initial_dx, initial_dy):
    """approximate the position of x when the ball touch the ground (y = 0)"""
    s_y = s.get_y()
    s_x = s.get_x()
    while round(s_y) < 0:
        s_y += 0.1 * initial_dy
        s_x += 0.1 * initial_dx
    return round(s_x)

# MAIN

cannon = Cannon(12, 0)
target = Target(60, 0)
ball = Cannonball(cannon.get_x() + 1, cannon.get_y() + 1)

max_x = max(cannon.get_x(), target.get_x(), ball.get_x())
max_y = max(cannon.get_y(), target.get_y(), ball.get_y())

battlefield = Display((max_x + 5), (max_y + 5))

battlefield.add_sprite(cannon)
battlefield.add_sprite(target)
battlefield.add_sprite(ball)

dx, dy = calculate_moving_vectors(battlefield)
initial_dy = dy
initial_dx = dx
update_position = 0

while not ball_out_of_field(ball, battlefield):
    update_display(battlefield)
    ball.update_position(dx, dy)
    update_position += 1
    if update_position > 2 :
        dy, dx = applicate_friction(dy, initial_dy, dx, initial_dx)

# ball is on the ground or out of sight
# remove it from de sprites of the field
battlefield.remove_sprite(ball)

if ball.get_y() <= 0:
    x_impact = determine_x(ball, initial_dx, initial_dy)
    # create an instance of the class impact
    impact = Impact(x_impact, 0)
    # add a new sprite to the field
    battlefield.add_sprite(impact)
    update_display(battlefield)
    print()
    print("ball touch the ground")
else:
    update_display(battlefield)
    print()
    print("ball touch the ground")