class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return point
    
    def __sub__(self, other):
        return point
    
    def __mul__(self, other):
        return point

    def __str__(self, other):
        return point
    
class rectangle(point):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    

rec1 = rectangle(0,0,5,6)
rec2 = rectangle(5,9,8,12)
  
rec3 = rec2 + rec1