from Agents.MovingAgent import MovingAgent
from Ships.Ship import Ship

class TradingAgent(MovingAgent):
    def __init__(self, name=None, ship=None, image=None, world=None):
        MovingAgent.__init__(self, name, prefix="Pilot ", suffix="", image=image, world=world)
        self.ship = ship if ship is not None else Ship()

