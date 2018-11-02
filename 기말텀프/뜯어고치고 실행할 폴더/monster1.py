import game_framework
from pico2d import *
from ball import Ball

import random
import math

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# Boy States

class IdleState:

    @staticmethod
    def enter(monster1, event):
        monster1.timer = get_time()

    @staticmethod
    def exit(monster1, event):
        pass

    @staticmethod
    def do(monster1):
        pass

    @staticmethod
    def draw(monster1):
        monster1.image.draw(monster1.x, monster1.y)


class Monster1:

    def __init__(self):
        self.x, self.y = 0, 300
        self.image = load_image('monster1.png')
        self.width = 0
        self.high = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)


