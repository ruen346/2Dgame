from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_x(x):
    pass

def move_y(y):
    pass

def move_character(x, y):
    move_x()
    move_y()

def move_character_return():
    pass

while True:
    move_character(203, 535)
    move_character(132, 243)
    move_character(535, 470)
    move_character(477, 203)
    move_character(715, 136)
    move_character(316, 225)
    move_character(510, 92)
    move_character(692, 518)
    move_character(682, 336)
    move_character(712, 349)
    move_character_return()
    
close_canvas()