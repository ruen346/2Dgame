import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state



name = "MainState"

image = None
tile1 = None
tile2 = None

boy = None
grass = None
pauses = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

    global image, tile1, tile2
    image = load_image('main_title.png')
    tile1 = load_image('tile2.png')
    tile2 = load_image('tile3.png')



def exit():
    global boy, grass
    del (boy)
    del (grass)

    global image
    del (image)


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)


def update():
    boy.update()


def draw():
    clear_canvas()

    image.draw(640, 360)

    for i in range(0,16):
        if game_framework.text2[i] == '0':
            tile1.draw((i % 4) * 128, 720 - (i // 4) * 128)
        elif game_framework.text2[i] == '1':
            tile2.draw((i % 4) * 128, 720 - (i // 4) * 128)

    grass.draw()
    boy.draw()

    update_canvas()