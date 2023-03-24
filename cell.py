from tkinter import Button
import random
import settings

class Cell:

    all = []

    def __init__(self, x, y, is_mine = False):

        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_button_object = None
        
        # Append the object to the Cell.all list

        Cell.all.append(self)

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

    @staticmethod

    def randomize_mines():

        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Overriding representation method

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
