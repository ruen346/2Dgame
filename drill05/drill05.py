from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def make_character(x, y, ch_x, ch_y):
    frame = 0


    go_x = (x - ch_x) / 10
    go_y = (y - ch_y) / 10

    for i in range(0,10):
        clear_canvas()
        if (ch_x < x):
            character.clip_draw(frame * 100, 100, 100, 100, ch_x, ch_y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, ch_x, ch_y)
        ch_x += go_x
        ch_y += go_y
        update_canvas()
        get_events()
        frame = (frame + 1) % 8
        delay(0.05)




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