import tkinter as tk
import numpy as np
from app.game_logic import GameOfLife

class AppGui(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Dimentions
        self.frame_width = 600
        self.frame_height = 600
        self.cell_size = 20
        self.grid_cols = self.frame_width // self.cell_size
        self.grid_rows = self.frame_height // self.cell_size

        # initialize grid
        self.grid = np.zeros((self.grid_rows, self.grid_cols))

        self.game_logic = GameOfLife(self.grid)

        # create widgets 
        self.create_widgets()

    # create widgets method
    def create_widgets(self):
        # initial frame setup
        self.frame = tk.Frame(width=self.frame_width, height=self.frame_height, bg="black")

        # Canvas cells grid
        self.canvas = tk.Canvas(self.frame,bg="purple", width=self.frame_width, height=500)
        self.canvas.bind("<Button-1>", self.handle_click)

        # checkbutton state
        self.check_status = tk.BooleanVar()
        self.check_status.set(True)

        # Buttons
        self.display_checkbutton = tk.Checkbutton(self.frame, text="Display Grid", variable=self.check_status, command=self.display_grid)
        self.play_button = tk.Button(self.frame, text="Start", command=self.game_logic)
        self.pause_button = tk.Button(self.frame, text="Pause")
        self.next_button = tk.Button(self.frame, text="Next", command=self.game_logic.next_generation)
        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_cells)

        # labels
        self.generation_label = tk.Label(self.frame, text="Generation: 0")
        self.population_label = tk.Label(self.frame, text="Populattion: 0")

        
        # Layout
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.canvas.grid(column=0, row=0, columnspan=6, pady=10)
        self.display_checkbutton.grid(column=0, row=1)
        self.play_button.grid(column=1, row=1)
        self.pause_button.grid(column=2, row=1)
        self.next_button.grid(column=3, row=1)
        self.clear_button.grid(column=4, row=1)
        self.generation_label.grid(column=5, row=1)
        self.population_label.grid(column=5, row=2)

        # draw initial grid
        self.draw_grid(self.grid_cols, self.grid_rows, "black")


    # draw grid method
    def draw_grid(self, cols, rows, outline_color):
        # iterate over each item in oue 2d Array
        for row_idx in range(rows):
             # iterate over each cell 
            for col_idx in range(cols):
                # calculate cells top-left and bottom-right coordinates 
                x0 = col_idx * self.cell_size
                y0 = row_idx * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # draw a rectangle
                self.canvas.create_rectangle(x0, y0, x1, y1, outline=outline_color, fill="white")

        

    # handle click to change celss colors
    def handle_click(self, event):
        # get outline color
        color = self.get_outline_color()

        # calculate col and row of clicked cell
        cell_row = event.y // self.cell_size
        cell_col = event.x // self.cell_size

        # validate click within grid bound
        if 0 <= cell_col < self.grid.shape[1] and 0 <= cell_row < self.grid.shape[0]:
            # toggle cell color
            if self.grid[cell_row, cell_col] == 0:
                self.grid[cell_row, cell_col] = 1  # update cell state to 1 (alive)
                fill_color = "black" # cell will change to this color when alive

            else:
                self.grid[cell_row, cell_col] = 0 # dead cell
                fill_color = "white" # default cell color 

            # calculate coordinates to draw the black cell
            x0 = cell_col * self.cell_size
            y0 = cell_row * self.cell_size
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size

            # update cell color
            self.canvas.create_rectangle(x0, y0, x1, y1, outline=color, fill=fill_color)

    def clear_cells(self):
        # change the state of every cell to 0
        self.grid.fill(0)

        # get outline color
        color = self.get_outline_color()

        # change the color of the cell by drawing the grid
        self.draw_grid(self.grid_cols, self.grid_rows, outline_color=color) 

    def display_grid(self):
        # get outline color
        color = self.get_outline_color()

        # draw the grid
        self.draw_grid(self.grid_cols, self.grid_rows, outline_color=color) 

    # helper method to get outline color based on the status of our grid
    def get_outline_color(self) -> str:
        # get the value of check_status
        status = self.check_status.get()

        if (status):
            outline_color = "black"
        
        else:
            outline_color = "white"

        return outline_color
    
        