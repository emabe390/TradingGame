
import pyglet
from Agents.Agent import Agent
from Helpers.Coordinate import Coordinate
from Graphics.GraphicalEntity import GraphicalEntity
import logging
import math

logger = logging.getLogger("mainLogger")
class MovingAgent(Agent, GraphicalEntity):
    def __init__(self, name=None, suffix=None, prefix=None, ship=None, image=None):
        Agent.__init__(self, name=name, suffix=suffix, prefix=prefix)
        GraphicalEntity.__init__(self)
        self.pos = Coordinate()
        self.ship = ship
        self.target = self.pos
        self.image = image

    def set_target(self, target):
        self.target = target
        self.alive = True

    def step(self, dt, batch):
        shouldUpdate = Agent.step(self, dt, batch)
        rotation = None
        if shouldUpdate:
            if self.target is not None:
                rotation = self._move(self.target, dt)
        #self.draw_text(batch, self.id, self.pos)
        self.draw_sprite(batch, self.image, self.pos, rotation)
        return shouldUpdate
        

    def _move(self, target, dt):
        if self.ship is not None:
            moveCoord = self.pos.deltaCoord(self.target, self.ship.velocity * dt * 120)
            if not moveCoord.isZero():
                self.pos = self.pos + moveCoord
                return math.atan2(moveCoord.y, -moveCoord.x)*180/math.pi
            else:
                #Enter location
                self.alive = False
