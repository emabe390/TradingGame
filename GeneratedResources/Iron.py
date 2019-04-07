class Iron():
    def __init__(self, units=0):
        self.name = "Iron"
        self.units = units
        self.volume = 15
        self.baseValue = 1

    def information(self):
        return {"name": self.name, "units": self.units, "volume": self.volume, "baseValue": self.baseValue}
