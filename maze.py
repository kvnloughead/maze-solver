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

    def create_maze(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True

        while True:
            neighbors = [(i+1, j, "bottom"), (i, j+1, "right"), (i-1, j, "top"), (i, j-1, "left")]
            possible_moves = []

            for n in neighbors:
                n_i, n_j, direction = n
                if n_i >= self._num_cols or n_j >= self._num_rows or n_i < 0 or n_j < 0:
                    continue
                n_cell = self._cells[n_i][n_j]
                if not n_cell.visited:
                    possible_moves.append((n_i, n_j, direction))

            if not possible_moves:
                break

            # Choose a random neighbor to move to
            move = random.choice(possible_moves)
            n_i, n_j, _ = move
            next_cell = self._cells[n_i][n_j]

            # Remove walls between the current cell and the chosen neighbor
            self._remove_adjacent_walls(curr_cell, i, j, next_cell, move)

            # Recursively break walls for the chosen neighbor
            self._break_walls_r(n_i, n_j)

    def _remove_adjacent_walls(self, curr_cell, i, j, next_cell, move):
        """Removes the wall between curr_cell and next_cell based on the direction."""
        n_i, n_j, direction = move
        if direction == "left":
            curr_cell.has_left_wall = False
            next_cell.has_right_wall = False
        elif direction == "right":
            curr_cell.has_right_wall = False
            next_cell.has_left_wall = False
        elif direction == "top":
            curr_cell.has_top_wall = False
            next_cell.has_bottom_wall = False
        elif direction == "bottom":
            curr_cell.has_bottom_wall = False
            next_cell.has_top_wall = False
        self._draw_cell(i, j, curr_cell)
        self._draw_cell(n_i, n_j, next_cell)

    def _have_adjacent_walls(self, curr_cell, next_cell, direction):
        """Checks if the current cell and next cell have walls between them."""
        if direction == "left":
            return curr_cell.has_left_wall and next_cell.has_right_wall
        elif direction == "right":
            return curr_cell.has_right_wall and next_cell.has_left_wall
        elif direction == "top":
            return curr_cell.has_top_wall and next_cell.has_bottom_wall
        elif direction == "bottom":
            return curr_cell.has_bottom_wall and next_cell.has_top_wall
        return False

    def _reset_cells_visited(self):
        """Resets visited status of all cells."""
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True

        # Define possible moves (grid indices and corresponding directions)
        neighbors = [
            (i, j+1, "right"),  # Move right
            (i+1, j, "bottom"), # Move down
            (i, j-1, "left"),   # Move left
            (i-1, j, "top")     # Move up
        ]

        for n_i, n_j, direction in neighbors:
            if n_i < 0 or n_j < 0 or n_i >= self._num_cols or n_j >= self._num_rows:
                continue

            next_cell = self._cells[n_i][n_j]
            
            # Check if the move is valid (i.e., no wall between cells)
            if not next_cell.visited and not self._have_adjacent_walls(curr_cell, next_cell, direction):
                curr_cell.draw_move(next_cell, fill_color="white")
                self._solve_r(n_i, n_j)
                
    def __str__(self):
        # Print self._cells in a readable format
        cell_strs = []
        for row in self._cells:
            cell_strs.append(" | ".join(str(cell) for cell in row))
        return "\n".join(cell_strs)
        
