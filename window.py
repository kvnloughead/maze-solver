from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self._canvas = Canvas(master=self.__root,
                              width=self._width, 
                              height=self._height)
        self._canvas.pack()
        self._running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
         self._running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

    def write(self, x, y, text):
        self._canvas.create_text(x, y, text=text)