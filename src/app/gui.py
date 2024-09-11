import tkinter as tk
import numpy as np
from app.game_logic import GameOfLife

class AppGui(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # control gui rendering
        self.is_running = False

        # Dimensions
        self.frame_width = 600
        self.frame_height = 600
        self.cell_size = 20
        self.grid_cols = self.frame_width // self.cell_size
        self.grid_rows = self.frame_height // self.cell_size

        # Initialize grid
        self.grid = np.zeros((self.grid_rows, self.grid_cols))

        self.game_logic = GameOfLife(self.grid)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Initial frame setup
        self.frame = tk.Frame(width=self.frame_width, height=self.frame_height, bg="black")

        # Canvas cells grid
        self.canvas = tk.Canvas(self.frame, bg="purple", width=self.frame_width, height=self.frame_height)
        self.canvas.bind("<Button-1>", self.handle_click)

        # Checkbutton state
        self.check_status = tk.BooleanVar()
        self.check_status.set(True)

        # Buttons
        self.display_checkbutton = tk.Checkbutton(self.frame, text="Display Grid", variable=self.check_status, command=self.display_grid)
        self.play_button = tk.Button(self.frame, text="Start", command=self.start_game)  
        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause_game)  
        self.next_button = tk.Button(self.frame, text="Next", command=self.render_next_gen)
        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_cells)

        # Labels
        self.generation_label = tk.Label(self.frame, text=f"Generation: {self.game_logic.generations}")
        self.population_label = tk.Label(self.frame, text=f"Population: {self.game_logic.population}")
        
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

        # Draw initial grid
        self.draw_grid(self.grid_cols, self.grid_rows, "black")

    def draw_grid(self, cols, rows, outline_color):
        # Iterate over each item in our 2D array
        for row_idx in range(rows):
            for col_idx in range(cols):
                x0 = col_idx * self.cell_size
                y0 = row_idx * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline=outline_color, fill="white")

    def handle_click(self, event):
        # variables
        color = self.get_outline_color()
        cell_row = event.y // self.cell_size
        cell_col = event.x // self.cell_size

        if 0 <= cell_col < self.grid.shape[1] and 0 <= cell_row < self.grid.shape[0]:
            if self.grid[cell_row, cell_col] == 0:
                self.grid[cell_row, cell_col] = 1
                fill_color = "black"
            else:
                self.grid[cell_row, cell_col] = 0
                fill_color = "white"

            x0 = cell_col * self.cell_size
            y0 = cell_row * self.cell_size
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size

            self.canvas.create_rectangle(x0, y0, x1, y1, outline=color, fill=fill_color)

    def clear_cells(self):
        # Clear the state matrix
        self.grid.fill(0)
        self.game_logic.state_matrix = np.zeros_like(self.grid)  # ensures the game logic state matrix is also cleared

        # Clear the canvas
        self.canvas.delete("all")
        
        # Draw the grid
        color = self.get_outline_color()
        self.draw_grid(self.grid_cols, self.grid_rows, outline_color=color)

        # stop game logic
        self.is_running = False

    def display_grid(self):
        color = self.get_outline_color()
        self.draw_grid(self.grid_cols, self.grid_rows, outline_color=color)

    def get_outline_color(self) -> str:
        return "black" if self.check_status.get() else "white"

    def render_next_gen(self):        
        # Update game logic state with the current grid state
        self.game_logic.state_matrix = self.grid.copy()  # Copying grid here

        # Compute the next generation
        self.game_logic.next_generation()

        # Update self.grid with the new state matrix from game logic
        self.grid = self.game_logic.state_matrix.copy()
        self.update_grid()

        # update labels
        self.generation_label.config(text=f"Generations: {self.game_logic.generations}")
        self.population_label.config(text=f"Population: {self.game_logic.population}")

    def update_grid(self):
        # Clear canvas before redraw
        self.canvas.delete("all")
        
        # Iterate over each cell in the grid
        for row_idx in range(self.grid_rows):
            for col_idx in range(self.grid_cols):
                # Get cell state
                cell_state = self.game_logic.state_matrix[row_idx, col_idx]

                # Handle fill and color
                fill_color = "black" if cell_state == 1 else "white"
                color = self.get_outline_color()

                # Calculate coordinates to draw the cell
                x0 = col_idx * self.cell_size
                y0 = row_idx * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # Redraw grid
                self.canvas.create_rectangle(x0, y0, x1, y1, outline=color, fill=fill_color)


    # start game update
    def start_game(self):
        # check for alive cells
        alive_cells = self._has_alive_cells()

        # start only if not already running and grid contains alive cells
        if not self.is_running and alive_cells:
            self.is_running = True
            self._update_game()

    # pause game update
    def pause_game(self):
        # pause if game logic is running
        if self.is_running:
            self.is_running = False

    # update game computations
    def _update_game(self):
        if self.is_running:
            self.render_next_gen() # computations
            self.master.after(200, self._update_game) #schedule next computations

    # check for alive cells in grid
    def _has_alive_cells(self)-> bool:
        # check for alive cells
        alive_cells = np.any(self.grid == 1) 
        
        return alive_cells