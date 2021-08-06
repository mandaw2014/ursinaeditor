from ursina import *
from editor_level import *
from rpc import *

app = Ursina()
e = EditorCamera()

game_objects = []

def input(key):
    if key == "n":
        c = EditorCube()
        game_objects.append(c)

PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

Sky()
app.run()