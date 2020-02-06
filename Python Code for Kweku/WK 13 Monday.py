from math import pi
class sphere:
    def __init__(self,radius):
        self.radius = radius
        self.area= 0
        self.volume= 0
    
    def getRadius(self):
        return self.radius
    
    
    def surfaceArea(self):
        r = self.radius
        self.area = 4 * pi * r**2
        return (self.area)


    def getVolume(self):
        r=self.radius
        self.volume=(r**3) * pi * 4/3
        return self.volume
    


def main():
    sph=sphere(5)
    print("sa","{0:0.02f}".format(sph.surfaceArea()))
    print("vol","{0:0.02f}".format(sph.getVolume()))
    
    
main()
    
    
class cube:
    def __init__(self, length):
        self.Length = length
        self.SurfaceArea= 0
        self.Volume= 0
        
    def getLength(self):
        return self.Length
    
    def surfaceArea(self):
        l = self.Length
        self.SurfaceArea= l ** 2 * 6
        return self.SurfaceArea
        

    def volume(self):
        self.Volume = self.Length ** 3
        return self.Volume
    
def main():
    hp= cube(7)
    print("surface area", hp.surfaceArea())
    print("surface area", hp.volume())
    
main()
