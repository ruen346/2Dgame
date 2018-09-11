from pico2d import *
import math
open_canvas()

image = load_image('character.png')
image2 = load_image('grass.png')
while(1):
    for x in range(400,800,10):
        clear_canvas_now()
        image.draw_now(x,90)
        image2.draw_now(400,30)
        delay(0.01)
    for y in range(0,490,10):
        clear_canvas_now()
        image.draw_now(800,y)
        image2.draw_now(400,30)
        delay(0.01)
    for x in range(800,0,-10):
        clear_canvas_now()
        image.draw_now(x,490)
        image2.draw_now(400,30)
        delay(0.01)
    for y in range(490,0,-10):
        clear_canvas_now()
        image.draw_now(0,y)
        image2.draw_now(400,30)
        delay(0.01)
    for x in range(0,400,10):
        clear_canvas_now()
        image.draw_now(x,90)
        image2.draw_now(400,30)
        delay(0.01)

    for i in range(0,3600,20):
        x = math.sin(i/360) * 100
        y = math.cos(i/360) * 100
        clear_canvas_now()
        image.draw_now(x + 400,y + 90 + 140)
        image2.draw_now(400,30)
        delay(0.01)
    
close_canvas()
