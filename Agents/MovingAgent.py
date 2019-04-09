
import pyglet
from Agents.Agent import Agent
from Helpers.Coordinate import Coordinate
from Graphics.GraphicalEntity import GraphicalEntity
import logging
import math

logger = logging.getLogger("mainLogger")
class MovingAgent(Agent, GraphicalEntity):
    def __init__(self, name=None, suffix=None, prefix=None, ship=None, image=None, world=None):
        Agent.__init__(self, name=name, suffix=suffix, prefix=prefix)
        GraphicalEntity.__init__(self)
        self.world = world
        self.position = Coordinate()
        self.ship = ship
        self.target = self.position
        self.image = image

    def set_target(self, target):
        self.target = target
        self.alive = True

    def step(self, dt, batch, draw=True):
        shouldUpdate = Agent.step(self, dt, batch)
        rotation = None
        if shouldUpdate:
            rotation = self._move(self.target, dt)
        #self.draw_text(batch, self.id, self.pos)
        if draw:
            self.draw_sprite(batch, self.image, self.position, rotation)
        return shouldUpdate
        

    def _move(self, target, dt):
        if self.ship is not None:
            dt_left = dt
            while dt_left > 0:
                moveCoord, perc_dt_left = self.position.deltaCoord(self.target, self.ship.velocity * dt * 120)
                dt_left = dt_left * perc_dt_left
                if not moveCoord.isZero():
                    self.position = self.position + moveCoord
                    return math.atan2(moveCoord.y, -moveCoord.x)*180/math.pi
                else:
                    self.target = self.world.get_random_location().position
