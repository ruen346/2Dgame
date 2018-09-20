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
    global ch_x
    global ch_y
    global go_x
    global go_y
    global count

    count = 30
    go_x = (x - ch_x) / 30
    go_y = (y - ch_y) / 30

def click_mouse():
    global mouse_x
    global mouse_y
    make_character(mouse_x, mouse_y)

def handle_events():
    pass

while running:
    handle_events()
    clear_canvas()

    if count > 0:
        ch_x += go_x
        ch_y += go_y
        count -= 1

    kpu.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if (go_x > 0):
        character.clip_draw(frame * 100, 100, 100, 100, ch_x - 25, ch_y + 25)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, ch_x - 25, ch_y + 25)

    hand.draw(mouse_x, mouse_y)

    update_canvas()
    get_events()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()