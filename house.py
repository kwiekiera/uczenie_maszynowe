from property import Property

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + "Rozmiar działki: {}".format(self.plot)