from __future__ import annotations  # https://stackoverflow.com/a/33533514/2470878
import math
from pyglet import shapes


def lerp(a, b, percent):
    return percent * (b - a)


def clamp(x, min, max):
    if x > max:
        return max
    elif x < min:
        return min
    else:
        return x


class P:
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def lerp(self, to, percent):
        """Return delta to next interpolation point"""
        dx = lerp(self.x, to.x, percent)
        dy = lerp(self.y, to.y, percent)

        return P(dx, dy)

    def clamp(self, max):
        """Return clamped vector"""
        length = self.length()
        if length > max:
            d = max / length
        else:
            d = 1
        return P(self.x * d, self.y * d)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Object:
    def __init__(self, position: P):
        self.position = position
        self.childrens = []

    def update(self, dt):
        pass

    def move(self, delta: P):
        self.position.x += delta.x
        self.position.y += delta.y

        for c in self.childrens:
            c.move(delta)

    def draw(self, batch):
        pass

    def add_to_batch(self, batch):
        for c in self.childrens:
            c.add_to_batch(batch)

    def add_child(self, child: Object):
        self.childrens.append(child)


class Line(Object):
    def __init__(self, a: P, b: P):
        super().__init__(a)

        self.a = a
        self.b = b

        self._line = None

    def add_to_batch(self, batch):
        super().add_to_batch(batch)

        self._line = shapes.Line(
            self.a.x,
            self.a.y,
            self.b.x,
            self.b.y,
            width=4,
            color=(200, 20, 20),
            batch=batch,
        )

    def move(self, delta: P):
        super().move(delta)

        self.a.x += delta.x
        self.a.y += delta.y
        self.b.x += delta.x
        self.b.y += delta.y

        if self._line:
            self._line.x = self.a.x
            self._line.y = self.a.y
            self._line.x2 = self.b.x
            self._line.y2 = self.b.y


class Circle(Object):
    def __init__(self, center: P, radius: int):
        super().__init__(center)

        self.center = center
        self.radius = radius

        self._circle = None

    def add_to_batch(self, batch):
        super().add_to_batch(batch)

        self._circle = shapes.Circle(
            self.center.x,
            self.center.y,
            self.radius,
            color=(200, 20, 20),
            batch=batch,
        )

    def move(self, delta: P):
        super().move(delta)

        self.center.x += delta.x
        self.center.y += delta.y

        if self._circle:
            self._circle.x = self.center.x
            self._circle.y = self.center.y
