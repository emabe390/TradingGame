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
from Helpers.Coordinate import Coordinate
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
        print(1/dt)
        batch = pyglet.graphics.Batch()
        self.running = self.world.step(dt, batch)
        #image = ResourceLoader.load_resources()["square"]
        #self.draw_sprite(batch, image, Coordinate(0,0))
        self.batch = batch
       # print("sleeping + drawing: %s, math: %s, diff %s" % (dt, t, dt-t))

class World():
    def __init__(self):
        resources = ResourceLoader.load_resources()
        self.locations = {}
        self.location_ids = []
        n = 5
        for x in range(n):
            for i in range(n):
                #if random.randint(0,101) > 20:
                #    continue
                location = Location(name="", image=resources["station"], position=Coordinate())
                self.locations[location.id] = location
                self.location_ids.append(location.id)
        self.agents = {}
        for _ in range(150):
            agent = TradingAgent(image=resources["ship"])
            self.agents[agent.id] = agent

    def set_target(self, target):
        for agent in self.agents.values():
            agent.set_target(target)

    def get_random_location(self):
        random_location_id_index = random.randint(0, len(self.location_ids)-1)
        random_location_id = self.location_ids[random_location_id_index]
        random_location = self.locations[random_location_id]
        return random_location

    def step(self, dt, batch):
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