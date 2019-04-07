class Steel():
    def __init__(self, units=0):
        self.name = "Steel"
        self.units = units
        self.volume = 100
        self.baseValue = 10

    def information(self):
        return {"name": self.name, "units": self.units, "volume": self.volume, "baseValue": self.baseValue}
