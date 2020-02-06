from math import *

print("This program will determine the surface area and volume represented in a solid sphere. ")

class Spheres:
    def __init__(self, r):
        self.radius = radius
        self.area = 0
        self.volume = 0
        
    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        r = self.radius
        self.area = 4 * 3.14 * (r*r)
        return (self.area)
    
    def getVolume(self):
        r = self.radius
        self.volume = (4/3) * 3.14 * (r * r * r)
        return (self.volume)
    
    def main():
        r = input("Please Enter the Radius of the Sphere: ")
        s = Spheres(r)
        print("the volume of the sphere is: ", s.surfaceArea())
        print("The surface area of the sphere is: ", s.volume())
        
    if __name__ == '__main__':
        main()
