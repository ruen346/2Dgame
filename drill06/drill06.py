from pico2d import *

open_canvas(1280,1024)

character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
kpu = load_image('KPU_GROUND.png')

hide_cursor()

ch_x = 0
ch_y = 0
go_x = 0
go_y = 0
running = True
frame = 0
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
mouse_x = 0
mouse_y = 0
count = 0

def make_character(x, y):
    pass

def click_mouse():
    make_character(mouse_x, mouse_y)

def handle_events():
    pass

while running:
    handle_events()

close_canvas()