import pyglet
from pyglet.window import key

from engine.basics import Object
from engine.input import mouse_pos


class Engine(pyglet.window.Window):
    def __init__(self) -> None:
        super().__init__(caption="Wanna see some art?")

        self.batch = pyglet.graphics.Batch()

        self.objects = []

    def update(self, dt):
        for o in self.objects:
            o.update(dt)

    def on_draw(self):
        self.clear()

        for o in self.objects:
            o.draw(self.batch)

        self.batch.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_mouse_motion(self, x, y, dx, dy):
        mouse_pos.x = x
        mouse_pos.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        mouse_pos.x = x
        mouse_pos.y = y
        # if button == mouse.LEFT:
        # print("The left mouse button was pressed.")

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()

    def add_object(self, object: Object):
        object.add_to_batch(self.batch)
        self.objects.append(object)


class Drawer:
    def __init__(self, batch) -> None:
        self.batch = batch
