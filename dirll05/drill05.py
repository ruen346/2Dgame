from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def make_character(x, y, ch_x, ch_y):
    pass

while True:
    make_character(132, 243, 203, 535)
    make_character(535, 470, 132, 243)
    make_character(477, 203, 535, 470)
    make_character(715, 136, 477, 203)
    make_character(316, 225, 715, 136)
    make_character(510, 92, 316, 225)
    make_character(692, 518, 510, 92)
    make_character(682, 336, 692, 518)
    make_character(712, 349, 682, 336)
    make_character(203, 535, 682, 336)
    
close_canvas()