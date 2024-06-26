import math

class Point:
  def __init__(self, x , y):
    self.x = x 
    self.y = y
    
  def to_center(self):
    return math.pow(math.pow(self.x,2) + math.pow(self.y,2), 0.5)

  def getPoint(self):
    return [self.x, self.y]
  
class PointColor(Point):
  def __init__(self, x, y, color):
      self.color = color 
      super().__init__(x,y)  


point = PointColor(2,3, "red") 
print(point.to_center())

point1 = Point(3,4)
print(point.getPoint())


