import pygame as pg
import moderngl as mgl
import time 
import sys
from model import *
from camera import Camera
from light import Light
import os



class Engine:
    def __init__(self, window_size=(1600, 900)):
    
        pg.init()
        self.WIN_SIZE = window_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        self.window = pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF )
        pg.event.set_grab(True)
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.delta_time = 0 
        self.light = Light()
        self.time = 0 
        self.camera = Camera(self)
        self.scene = Rectangle(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()
            if (event.type == pg.KEYDOWN and event.key == pg.K_h):
                time_taken = time.localtime().tm_sec
                save_name = f"screenshots/{time_taken}.png"
                pg.image.save(self.window, save_name)
    
    def render(self):
        #clear frame buffer
        #self.ctx.clear(color=(0.71,0.18,0.36))
        self.ctx.clear(color=(0, 0, 0.99))
        self.scene.render()

        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        CHECK_FOLDER = os.path.isdir("screenshots")
        if not CHECK_FOLDER:
            os.makedirs("screenshots")

        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = Engine()
    app.run()


