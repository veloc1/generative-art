from engine import Engine
from cursor import Cursor

if __name__ == "__main__":
    engine = Engine()

    engine.add_object(Cursor())

    engine.run()
