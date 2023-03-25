from tkinter import Button
import random
import settings

class Cell:

    # List with all Cell class instances

    all = []

    # Constructor

    def __init__(self, x, y, is_mine = False):

        # Attributes

        self.is_mine = is_mine # Cell Object Is or Is Not a Mine
        self.x = x # Cell Object Identifier (X position on Grid)
        self.y = y # Cell Object Identifier (Y position on Grid)
        self.cell_button_object = None # Cell Object Button Object
        
        # Append the object to the Cell.all list

        Cell.all.append(self)

    # Method to create Button Object

    def create_button_object(self, location):

        button = Button(
            location,
            width = 12,
            height = 4,
        )  

        # Button Object Behaviors 

        button.bind('<Button-1>', self.left_click_actions)
        button.bind('<Button-3>', self.rigth_click_actions)

        # Assigning Button Object to Cell Object
              
        self.cell_button_object = button

    # Method with actions to do when Button Object of Cell Object is left-clicked

    def left_click_actions(self, event):

        if self.is_mine:
            
            self.show_mine()

    # Method to interrupt the game and display message that player lost

    def show_mine(self):

        self.cell_button_object.configure(bg = 'red')

    # Method with actions to do when Button Object of Cell Object is rigth-clicked
    
    def rigth_click_actions(self, event):
        
        print(event)
        print("I am rigth click")

    @staticmethod

    # Method to randomize mines

    def randomize_mines():

        # Gets a random sample of Cell Objects to assign them Mine Status

        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Overriding representation method

    def __repr__(self):

        return f"Cell({self.x}, {self.y})"
