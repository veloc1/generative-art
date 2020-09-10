from engine.basics import Object, Circle, P
from engine.input import mouse_pos


class Cursor(Object):
    def __init__(self) -> None:
        super().__init__(P(30, 30))
        self.add_child(Circle(self.position, 10))

    def update(self, dt):
        d = self.position.lerp(mouse_pos, 1 * dt)
        # d = d.clamp(4)
        self.move(d)
        # self.move(P(0.1, 0.1))
