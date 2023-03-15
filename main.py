from tkinter import *
import settings
import utils

# Instantiating a window instance

root = Tk()

# Changing window background color

root.configure(bg = "black")

# Changing window size and title

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper game")

# Prohibiting window resizing

root.resizable(False, False)

# Creating top frame

top_frame = Frame(
    root,
    bg = 'red', # Change later to black
    width = utils.window_dimensions_percentage(True, 100),
    height = utils.window_dimensions_percentage(False, 25)
)

top_frame.place(x = 0, y = 0)

# Creating left frame

left_frame = Frame(
    root,
    bg = 'blue', # Change later to black
    width = utils.window_dimensions_percentage(True, 25),
    height = utils.window_dimensions_percentage(False, 75)
)

left_frame.place(x = 0, y = utils.window_dimensions_percentage(False, 25))

# Running the window

root.mainloop()
