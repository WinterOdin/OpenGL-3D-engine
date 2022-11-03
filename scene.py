from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        n, s = 40, 3

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
                #add(MovingCube(app, pos=(x, -s, z), scale=(2, 2, 2), tex_id=1))

        self.moving_cube = MovingCube(app, pos=(0, 3, -10), scale=(2, 2, 2), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
