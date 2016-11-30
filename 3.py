# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid:

    def __init__(self, a, b, c):
        self.a_side = a
        self.b_side = b
        self.c_side = c
        self.surface = 0
        self.volume = 0

        self.getSurface()
        self.getVolume()

    def getSurface(self):
        self.surface = 2 * (self.a_side * self.b_side + self.a_side * self.c_side + self.c_side * self.b_side)

    def getVolume(self):
        self.volume = self.a_side * self.b_side + self.c_side

cube = Cuboid(10, 20, 30)
print (cube.surface)
print (cube.volume)
