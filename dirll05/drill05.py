from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

ch_x = 0
ch_y = 0

def move_x(x):
    frame = 0
    if(ch_x < x):
        while ch_x < x:
            clear_canvas()
            character.clip_draw(frame * 100, 100, 100, 100, x, ch_y)
            update_canvas()
            x += 1
            delay(0.002)
            frame = (frame+1) % 8
            get_events()
            
    elif (ch_x >= x):
        while ch_x > x:
            clear_canvas()
            character.clip_draw(frame * 100, 0, 100, 100, x, ch_y)
            update_canvas()
            x -= 1
            delay(0.002)
            frame = (frame + 1) % 8
            get_events()

def move_y(y):
    pass

def move_character(x, y):
    move_x(x)
    move_y(y)

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