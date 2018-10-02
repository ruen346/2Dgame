from pico2d import *
import random

open_canvas(1280,1024)

character = load_image('animation_sheet.png')

hide_cursor()

running = True
frame = 0
ch_x = 0
ch_y = 0


def move_character(x,y):
    pass


def go_character(p1,p2):
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        move_character((x,y))
        delay(0.05)

size = 20
points = [(random.randint(-500,500), random.randint(-350, 350)) for i in range(size)]
n = 1

while running:

    clear_canvas()

    if (ch_x > points[n - 1]):
        character.clip_draw(frame * 100, 100, 100, 100, ch_x - 25, ch_y + 25)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, ch_x - 25, ch_y + 25)

    go_character(points[n - 1], points[n])
    n = (n + 1) % size

    update_canvas()
    get_events()
    frame = (frame + 1) % 8

close_canvas()