class Building:

    South, West, Width_WE, Width_NS, Height = 0,0,0,0,0

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.South, self.West, self.Width_WE, self.Width_NS, self.Height = south, west, width_WE, width_NS, height

    def corners(self):
        dic = {}
        dic["south-east"] = [self.South, self.West + self.Width_WE]
        dic["north-east"] = [self.South + self.Width_NS, self.West + self.Width_WE]
        dic["south-west"] = [self.South, self.West]
        dic["north-west"] = [self.South + self.Width_NS, self.West]
        return dic

    def area(self):
        return self.Width_WE * self.Width_NS

    def volume(self):
        return self.Width_WE * self.Width_NS * self.Height

    def __repr__(self):
        return "Building({0}, {1}, {2}, {3}, {4})".format(self.South, self.West, self.Width_WE, self.Width_NS, self.Height)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"