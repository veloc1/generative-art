import pyglet
from pyglet import shapes
from pyglet.window import mouse, key


window = pyglet.window.Window(caption="Wanna see some art?")
batch = pyglet.graphics.Batch()


line2 = shapes.Line(150, 150, 444, 111, width=4, color=(200, 20, 20), batch=batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    print("A key was pressed")
    if symbol == key.A:
        print('The "A" key was pressed.')


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed.")


pyglet.app.run()
