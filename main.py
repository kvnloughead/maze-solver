from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    print(cell1)
    cell1.draw(10, 10, 50, 50, "green")
    print(cell1)

    cell2 = Cell(win)
    cell2.draw(60, 60, 120, 120, "green")

    cell1.draw_move(cell2, False)    
    win.wait_for_close()

if __name__ == "__main__":
    main()