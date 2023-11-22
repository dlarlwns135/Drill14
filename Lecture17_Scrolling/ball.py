from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def set_background(self, bg):
        # fill here
        self.bg = bg
        # self.x = self.bg.w / 2
        # self.y = self.bg.h / 2
        pass
    def draw(self):
        # self.image.draw(self.x, self.y)
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.clip_draw(0, 0, 21, 21, sx, sy)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                game_world.remove_object(self)
                pass
            case 'zombie:ball':
                other.ball = self