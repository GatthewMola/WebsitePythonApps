class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        """Draws the shape into the canvas"""
        # This piece of code is essentially the "data[0:3, 0:2]" type code we used in the
        # array_to_numpy file. However, we are changing out the slice method and inputing our own
        # values based on the attributes defined in the init statement.
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color