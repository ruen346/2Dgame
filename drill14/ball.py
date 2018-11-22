import random
from pico2d import *
import game_world
import game_framework
import boy
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(450, 2050-1), random.randint(450, 1450-1), 0

    def get_bb(self):


    def draw(self):


    def update(self):
        pass

