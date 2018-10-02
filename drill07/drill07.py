from pico2d import *
import random

open_canvas(1280,1024)

character = load_image('animation_sheet.png')

hide_cursor()

running = True
frame = 0
ch_x = 0
ch_y = 0


def move_character(x2,y2):
    global ch_x
    global ch_y

    ch_x = x2
    ch_y = y2

def go_character(p1,p2):
    global frame
    global ch_x
    global ch_y
    for i in range(0, 100 + 1, 10):
        t = i / 100
        x2 = (1-t)*p1[0]+t*p2[0]
        y2 = (1-t)*p1[1]+t*p2[1]

        move_character(x2,y2)

        clear_canvas()
        if (ch_x > i):
            character.clip_draw(frame * 100, 100, 100, 100, ch_x - 25, ch_y + 25)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, ch_x - 25, ch_y + 25)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


size = 20
points = [(random.randint(0,1000), random.randint(0, 800)) for i in range(size)]
n = 1

ch_x,ch_y = points[n-1]

while running:

    i,j = points[n]

    go_character(points[n - 1], points[n])
    n = (n + 1) % size

close_canvas()