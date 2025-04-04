class Line:
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, 
                           fill=fill_color, width=2)
        
    def __str__(self):
        return f"Line({self.p1}, {self.p2})"
        