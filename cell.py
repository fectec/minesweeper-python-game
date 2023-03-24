from tkinter import Button

class Cell:

    def __init__(self, x, y, is_mine = False):

        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_button_object = None

    def create_button_obtect(self, location):

        button = Button(
            location,
            width = 12,
            height = 4,
            text = f"{self.x}, {self.y}"
        )  

        button.bind('<Button-1>', self.left_click_actions)
        button.bind('<Button-3>', self.rigth_click_actions)

        self.cell_button_object = button

    def left_click_actions(self, event):
        print(event)
        print("I am left click")

    def rigth_click_actions(self, event):
        print(event)
        print("I am rigth click")