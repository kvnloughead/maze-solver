from line import Line
from point import Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self._drawn = False
        self._window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self._upper_left = Point(x1, y1)
        self._upper_right = Point(x2, y1)
        self._lower_right = Point(x2, y2)
        self._lower_left = Point(x1, y2)
        self._center = Point((x1 + x2) / 2, (y1 + y2) / 2)

        def draw_wall(has_wall, p1, p2):
            if has_wall:
                self._window.draw_line(Line(p1, p2), fill_color)

        draw_wall(self.has_left_wall, self._upper_left, self._lower_left)
        draw_wall(self.has_top_wall, self._upper_left, self._upper_right)
        draw_wall(self.has_right_wall, self._upper_right, self._lower_right)
        draw_wall(self.has_bottom_wall, self._lower_left, self._lower_right)
        self._drawn = True

    def draw_move(self, to_cell, undo=False, fill_color="grey"):
        """Draws a path from the center of the current cell to the center of to_cell. Must not be called until the cell has been drawn."""
        if not self._drawn or not to_cell._drawn:
            raise Exception("Can't draw a move if either cell is not drawn")
        if undo:
            fill_color = "red"
        self._window.draw_line(Line(self._center, to_cell._center), fill_color)

    def walls(self):
        """Returns a list of Booleans corresponding to the cell's walls, in this order: ["top", "right", "bottom", "left"]."""
        return [self.has_top_wall, self.has_right_wall, self.has_bottom_wall, self.has_left_wall]

    def __str__(self):
        if not self._drawn:
            return "Cell()"
        else:
            return f"Cell({self._upper_left}, {self._upper_right}, {self._lower_right}, {self._lower_left})"