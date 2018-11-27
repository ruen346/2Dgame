import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state

import main_state


boy = None

name = "WorldBuildState"

rank = None

def enter():
    global rank
    rank = load_image('ranking_sp.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            game_framework.change_state(main_state)


def update():
    pass

def draw():
    font1 = load_font('ENCR10B.TTF', 20)
    clear_canvas()
    rank.draw(get_canvas_width()//2, get_canvas_height()//2)
    font1.draw(500, 700, "! > _ < ! 1등 : " + str(game_framework.ranking_score[0]), (0, 0, 0))
    font1.draw(500, 650, "> _ < 2등 : " + str(game_framework.ranking_score[1]), (0, 0, 0))
    font1.draw(500, 600, "> _ < 3등 : " + str(game_framework.ranking_score[2]), (0, 0, 0))
    font1.draw(500, 550, "> _ < 4등 : " + str(game_framework.ranking_score[3]), (0, 0, 0))
    font1.draw(500, 500, "> _ < 5등 : " + str(game_framework.ranking_score[4]), (0, 0, 0))
    font1.draw(500, 450, "> _ < 6등 : " + str(game_framework.ranking_score[5]), (0, 0, 0))
    font1.draw(500, 400, "> _ < 7등 : " + str(game_framework.ranking_score[6]), (0, 0, 0))
    font1.draw(500, 350, "> _ < 8등 : " + str(game_framework.ranking_score[7]), (0, 0, 0))
    font1.draw(500, 300, "> _ < 9등 : " + str(game_framework.ranking_score[8]), (0, 0, 0))
    font1.draw(500, 250, "ㅠ _ ㅠ 10등 : " + str(game_framework.ranking_score[9]), (0, 0, 0))
    update_canvas()