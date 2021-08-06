from ursina import *

class GameObject(Entity):
    def __init__(self, model, position, color):
        super().__init__()

        self.model = model
        self.position = position
        self.color = color

class EditorCube(GameObject):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            position = position,
            color = color.light_gray
        )

    def input(self, key):
        if held_keys["up arrow"]:
            self.z += 0.5
        if held_keys["down arrow"]:
            self.z -= 0.5
        if held_keys["left arrow"]:
            self.x -= 0.5
        if held_keys["right arrow"]:
            self.x += 0.5

        if held_keys["q"]:
            self.y -= 0.5
        if held_keys["e"]:
            self.y += 0.5

        if held_keys["+"]:
            self.scale_x += 0.01
            self.scale_y += 0.01
            self.scale_z += 0.01

        if held_keys["-"]:
            self.scale_x -= 0.01
            self.scale_y -= 0.01
            self.scale_z -= 0.01

            if self.scale_x <= 0.001 or self.scale_y <= 0.001 or self.scale_z <= 0.001:
                self.scale = (0.01, 0.01)
                return
                