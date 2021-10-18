#Fill in the Line class methods to accept coordinates as a pair of tuples and 
#return the slope and distance of the line.


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
         
    
    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self): # get the x and y coordinates
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return (x2-x1)/(y2-y1)

# output

coordinate1 = (3,2)
coordinate2 = (8,10)

#instance
li = Line(coordinate1,coordinate2)

print("the distance between the point is:\n {}" .format(li.distance()))
print()
print("the slope of the line is: {}" .format(li.slope()))
print()