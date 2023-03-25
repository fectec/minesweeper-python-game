from tkinter import Button, Label
import random
import settings

class Cell:

    # List with all Cell class instances

    all = []

    # Self-explanatory

    cell_count_label_object = None

    # Cell count variable

    cell_count = settings.CELL_COUNT

    # Constructor

    def __init__(self, x, y, is_mine = False, is_opened = False, is_marked = False):

        # Attributes

        self.x = x # Cell Object Identifier (X position on Grid)
        self.y = y # Cell Object Identifier (Y position on Grid)
        self.is_mine = is_mine # Cell Object Is or Is Not a Mine
        self.is_opened = is_opened # Cell Object Is or Is Not Opened
        self.is_marked = is_marked # Cell Object Is or Is Not Marked by the Player
        self.cell_button_object = None # Cell Object Button Object
        
        # Append the object to the Cell.all list

        Cell.all.append(self)

    # Method to return a Cell Object based on the value of X, Y
    
    def get_cell_by_axis(self, x, y):

        for cell in Cell.all:

            if cell.x == x and cell.y == y:

                return cell

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

    # Method to change a Cell Object Button Object Background Color
    
    def change_cell_color(self, color):

        self.cell_button_object.configure(bg = color)
    
    # Self-explanatory methods

    @staticmethod

    def create_cell_count_label(location):

        label = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells Left: {Cell.cell_count}",
            font = ("", 30)
        )

        Cell.cell_count_label_object = label

    @staticmethod

    def modify_cell_count_label_text(text):

        Cell.cell_count_label_object.configure(text = f"Cells Left: {text}")

    @staticmethod

    def decrease_cell_count(number):

        Cell.cell_count -= number

    # Method with actions to do when Button Object of Cell Object is left-clicked

    def left_click_actions(self, event):

        if self.is_mine:
            
            self.show_mine()

        else:

            if self.number_of_surrounding_mines == 0:

                for cell in self.surrounding_cells:

                    cell.show_number_of_surrounding_mines()

            self.show_number_of_surrounding_mines()
            
    # Method to interrupt the game and display message that player lost

    def show_mine(self):

        self.change_cell_color("red")

    @property

    # Method to get a list of Cell Objects that surround a Cell Object

    def surrounding_cells(self):

        # List of Cell Objects that surround a Cell Object

        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            ]

        #  Remove None values in cells list

        cells = [cell for cell in cells if cell is not None]

        return cells

    @property

    # Method to get the number of mines surrounding a Cell Object

    def number_of_surrounding_mines(self):

        counter = 0
       
        for cell in self.surrounding_cells:

            if cell.is_mine:

                counter += 1

        return counter
    
    # Method to show the number of mines surrounding a Cell Object

    def show_number_of_surrounding_mines(self):
        
        if not self.is_opened:  

            # Decrease cell count

            Cell.decrease_cell_count(1)

            self.cell_button_object.configure(text = f"{self.number_of_surrounding_mines}")
            
            # Replace the text of the cell count label with the newer count

            if Cell.cell_count_label_object:

                Cell.modify_cell_count_label_text(Cell.cell_count)

            # Marks the cell as opened

            self.is_opened = True

    # Method with actions to do when Button Object of Cell Object is rigth-clicked
    
    def rigth_click_actions(self, event):

        if not self.is_marked:

            self.change_cell_color("blue")
            self.is_marked = True

        else:

            self.change_cell_color("SystemButtonFace")
            self.is_marked = False

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
