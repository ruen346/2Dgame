import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state



name = "PauseState"

pauses = None
font = None


class Pause:
    def __init__(self):
        self.frame = 0

    def update(self):
        if self.frame == 50:
            self.frame = 0
        else:
            self.frame += 1

    def draw(self):
        if self.frame > 25:
            load_image('pause.png').draw(400, 400)


def enter():



def exit():



def handle_events():



def update():



def draw():
