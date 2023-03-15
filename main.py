from tkinter import *

# Instantiating a window instance

root = Tk()

# Changing window background color

root.configure(bg = "black")

# Changing window size and title

root.geometry('1440x720')
root.title("Minesweeper game")

# Prohibiting window resizing

root.resizable(False, False)

# Creating top frame

top_frame = Frame(
    root,
    bg = 'red', # Change later to black
    width = 1440,
    height = 180
)

top_frame.place(x = 0, y = 0)

# Creating left frame

left_frame = Frame(
    root,
    bg = 'blue', # Change later to black
    width = 360,
    height = 540
)

left_frame.place(x = 0, y = 180)

# Running the window

root.mainloop()
