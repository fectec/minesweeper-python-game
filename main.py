from tkinter import *
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

# Creating center frame

center_frame = Frame(
    root,
    bg = 'green', # Change later to black
    width = utils.window_dimensions_percentage(True, 75),
    height = utils.window_dimensions_percentage(False, 75)
)

center_frame.place(x = utils.window_dimensions_percentage(True, 25), y = utils.window_dimensions_percentage(False, 25))

# Running the window

root.mainloop()
