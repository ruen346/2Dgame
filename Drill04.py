from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 10
frame = 0
go = 0

while (1):
    clear_canvas()
    grass.draw(400, 30)
    if go == 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if go == 0:
        x += 10
    else:
        x -= 10

    if (x >= 800) & (go == 0):
        go = 1
    elif (x <= 0) & (go == 1):
        go = 0
    delay(0.05)
    get_events()

close_canvas()