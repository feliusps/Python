
# find the volume and area of a cylynder using oop the class get to inputs

class Cylinder:
    pi = 3.1416

    def __init__(self,height=1,radius=1): #use 1 as default
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * (self.radius)**2 * self.height

    def surface_area(self):
        top_area = self.pi * (self.radius)**2
        botton_area =  self.pi * (self.radius)**2
        side_area = 2*self.pi * self.radius * self.height
        return top_area + botton_area + side_area


# output
#instance
c = Cylinder(2,3)

print("The volume of the Cylinder is : {} " .format(c.volume()))

print("The surface area of the Cylinder is: {} " .format(c.surface_area()))

#printing in different format four decimals
print("Volume : %.4f, Area: %.4f" %(c.volume(), c.surface_area()))