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







close_canvas()