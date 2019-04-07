class Banana():
    def __init__(self, units=0):
        self.name = "Banana"
        self.units = units
        self.volume = 1
        self.baseValue = 0.1

    def information(self):
        return {"name": self.name, "units": self.units, "volume": self.volume, "baseValue": self.baseValue}
