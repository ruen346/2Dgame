from pico2d import *
import random

open_canvas(1280,1024)

character = load_image('animation_sheet.png')
kpu = load_image('KPU_GROUND.png')

hide_cursor()

running = True
frame = 0
ch_x = 0
ch_y = 0
fine = 0


def go_character(p1,p2,p3,p4):
    global frame
    global ch_x
    global ch_y
    global fine
    global points

    for i in range(0, 100, 2):
        t = i / 100
        x2 = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y2 = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

        ch_x = x2
        ch_y = y2

        clear_canvas()
        kpu.draw(1280 // 2, 1024 // 2)
        if (p2[0] < p3[0]):
            character.clip_draw(frame * 100, 100, 100, 100, ch_x - 25, ch_y + 25)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, ch_x - 25, ch_y + 25)

        for i in range(0,fine):
            cx, cy = points[i]
            character.clip_draw(0, 0, 100, 100, cx, cy)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)



size = 10
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]
n = 1

ch_x,ch_y = points[n-1]

while running:

    i,j = points[n]

    go_character(points[n - 3], points[n - 2], points[n-1], points[n])
    n = (n + 1) % size
    if(fine < 10):
        fine+=1

close_canvas()