import time, random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, 
                 window=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([Cell(self._win) for i in range(self._num_rows)])
        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j, cell)

    def _draw_cell(self, i, j, cell):
        """Draws cell (i, j). The origin of the maze is (self._x1, self._y1).
        From that, each cell is laid out according to their place in self._cells
        and their size."""
        if self._win == None:
            return
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)

    def _break_entrance_and_exit(self):
        choice = random.choice([0, 1])
        entrance, exit = self._cells[0][0], self._cells[-1][-1]
        if choice:
            entrance.has_left_wall = False
        else:
            entrance.has_top_wall = False

        choice = random.choice([0, 1])
        if choice:
            exit.has_right_wall = False
        else:
            exit.has_bottom_wall = False

        self._draw_cell(0, 0, entrance)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1, exit)

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)