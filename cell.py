from line import Line
from point import Point

class Cell:
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_top_wall = True 
        self.has_right_wall = True
        self.has_bottom_wall = True

        self._upper_left = p1
        self._upper_right = Point(p1.x, p2.y)
        self._lower_right = p2
        self._lower_left = Point(p2.x, p1.y)
        self._center = Point(min(p1.x, p2.x) + abs((p1.x - p2.x) / 2),
                             min(p1.x, p2.x) + abs((p1.y - p2.y) / 2))

        self._window = window

    def draw(self, fill_color="black"):
        def draw_wall(has_wall, p1, p2):
            if has_wall:
                self._window.draw_line(Line(p1, p2), fill_color)

        draw_wall(self.has_left_wall, self._upper_left, self._lower_left)
        draw_wall(self.has_top_wall, self._upper_left, self._upper_right)
        draw_wall(self.has_right_wall, self._upper_right, self._lower_right)
        draw_wall(self.has_bottom_wall, self._lower_left, self._lower_right)

    def draw_move(self, to_cell, undo=False, fill_color="grey"):
        """Draws a path from the center of the current cell to the center of to_cell."""
        if undo:
            fill_color = "red"
        self._window.draw_line(Line(self._center, to_cell._center), fill_color)

    def __str__(self):
        return f"Cell({self._upper_left}, {self._upper_right}, {self._lower_left}, {self._lower_right})"