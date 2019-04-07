import os
import time
import logging
import random
import pyglet
import Graphics.Engine as Engine
from Resources import ResourceLoader
from Agents.TradingAgent import TradingAgent
from Locations.Location import Location
from Graphics.GraphicalEntity import GraphicalEntity
from Helpers.Coordinate import Coordinate, Square
import time
logger = logging.getLogger("mainLogger")

class TradingGame(GraphicalEntity):
    def __init__(self):
        self.running = True
        self.frameCounter = 0
        self.world = World()
        self.batch = None
        Engine.gameObject = self

    def start(self):
        pyglet.app.run()

    def gameLoop(self, dt):
        #print(1/dt)
        batch = pyglet.graphics.Batch()
        self.running = self.world.step(dt, batch)
        #image = ResourceLoader.load_resources()["square"]
        #self.draw_sprite(batch, image, Coordinate(0,0))
        self.batch = batch
       # print("sleeping + drawing: %s, math: %s, diff %s" % (dt, t, dt-t))




class WorldSegment():
    def __init__(self, world, square=None, lx=None, ly=None, ux=None, uy=None):
        self.world = world
        if square is None:
            square = Square(lx, ly, ux, uy)
        self.square = square
        self.dt = 0
        self.entities = {}

    def add_entity(self, entity):
        self.entities[entity.name] = entity

    def remove_entity(self, entity):
        self.world.get_segment(entity.position).add_entity(entity)
        self.entities[entity.name].removed_from_segment(self)
        del self.entities[entity.name]

    def step(self, dt, batch):
        self.dt += dt
        in_frame = self.square.intersect(Engine.window_square)
        removable = []
        if in_frame or self.dt > 1:
            #print("drawin?")
            for entity in self.entities.values():
                entity.step(self.dt, batch, draw=True)
                if not self.square.inside(entity.position):
                    removable.append((self, entity))
            self.dt = 0
        return removable


class World():
    def __init__(self):
        resources = ResourceLoader.load_resources()

        self.segments = {}
        #n = 5
        self.segment_delta_x = 10
        self.segment_delta_y = 10
        #for x in range(-n, 2*n):
        #    for y in range(-n, 2*n):
        #        segment = WorldSegment(self,
        #                               lx=x*self.segment_delta_x, ly=y*self.segment_delta_y,
        #                               ux=(1+x)*self.segment_delta_x,uy=(1+y)*self.segment_delta_y)
        #        self.segments[(x,y)] = segment

        self.locations = {}
        self.location_ids = []
        n = 5
        for x in range(n):
            for i in range(n):
                #if random.randint(0,101) > 20:
                #    continue
                location = Location(name="", image=resources["station"], position=Coordinate(x*10,i*10))
                segment = self.get_segment(location.position)
                self.locations[location.id] = location
                self.location_ids.append(location.id)
                segment.add_entity(location)
                #self.segments[key].add_entity(location)

        self.agents = {}
        for _ in range(150):
            agent = TradingAgent(image=resources["ship"])
            self.agents[agent.id] = agent
            self.get_segment(agent.position).add_entity(agent)

    def get_segment(self, coordinate):
        key = (int(coordinate.x / self.segment_delta_y), int(coordinate.y / self.segment_delta_y))
        if key not in self.segments:
            self.segments[key] = WorldSegment(self, lx = key[0], ly = key[1], ux = key[0] + self.segment_delta_x, uy = key[1] + self.segment_delta_y)
        return self.segments[key]

    def set_target(self, target):
        for agent in self.agents.values():
            agent.set_target(target)

    def get_random_location(self):
        random_location_id_index = random.randint(0, len(self.location_ids)-1)
        random_location_id = self.location_ids[random_location_id_index]
        random_location = self.locations[random_location_id]
        return random_location

    def step(self, dt, batch):
        removable_pair = []
        for segment in self.segments.values():
            removable_pair.extend(segment.step(dt, batch))
        for segment, entity in removable_pair:
            segment.remove_entity(entity)
        return True
        anyAlive = False
        for _, agent in self.agents.items():
            if agent.alive is False:
                agent.set_target(self.get_random_location().position)
            anyAlive = agent.step(dt, batch) or anyAlive
        for _, location in self.locations.items():
            location.step(dt, batch)
        return anyAlive

    def get_all_entities(self):
        for id, agent in self.agents.items():
            yield id, agent

def main():
    game = TradingGame()   
    pyglet.clock.schedule_interval(game.gameLoop, 1/240.0)
    game.start()
    import time

def setup_logging():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

if __name__ == '__main__':
    setup_logging()
    #print("running release script")
    #import ReleaseScript
    #ReleaseScript.releaseScript()
    #from GeneratedResources.Iron import Iron
    #print(Iron().information())
    print("launching game...")
    main()