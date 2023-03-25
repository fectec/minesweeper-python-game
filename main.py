from tkinter import *
from cell import Cell
import settings
import utils

# Instantiating a window instance

root = Tk()

# Changing window background color

root.configure(bg = "black")

# Changing window size and title

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")

# Prohibiting window resizing

root.resizable(False, False)

# Creating top frame

top_frame = Frame(
    root,
    bg = 'black',
    width = utils.window_dimensions_percentage(True, 100),
    height = utils.window_dimensions_percentage(False, 25)
)

top_frame.place(x = 0, y = 0)

# Creating left frame

left_frame = Frame(
    root,
    bg = 'black', 
    width = utils.window_dimensions_percentage(True, 25),
    height = utils.window_dimensions_percentage(False, 75)
)

left_frame.place(x = 0, y = utils.window_dimensions_percentage(False, 25))

# Creating center frame

center_frame = Frame(
    root,
    bg = 'black',
    width = utils.window_dimensions_percentage(True, 75),
    height = utils.window_dimensions_percentage(False, 75)
)

center_frame.place(x = utils.window_dimensions_percentage(True, 25), y = utils.window_dimensions_percentage(False, 25))

# Creating Grid of Buttons

for i in range(settings.GRID_SIZE):
    for j in range(settings.GRID_SIZE):

        cell = Cell(i, j)
        cell.create_button_obtect(center_frame)
        cell.cell_button_object.grid(
            column = i,
            row = j
        )

Cell.randomize_mines()

# Running the window

root.mainloop()
