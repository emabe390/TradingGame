from Graphics.GraphicalEntity import GraphicalEntity
from Helpers import Coordinate, IdentifierGenerator

class Location(GraphicalEntity):
    def __init__(self, name, position, suffix=None, prefix=None, image=None):
        GraphicalEntity.__init__(self)
        self.image = image
        self.name = name
        self.id = IdentifierGenerator.next_id()
        if position is None:
            position = Coordinate.RandomCoordinate()
        self.position = position

    def step(self, dt, batch, draw=True):
        if draw:
            self.draw_sprite(batch, self.image, self.position)