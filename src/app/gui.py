import tkinter as tk

class AppGui(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Frame dimentions
        self.frame_width = 600
        self.frame_height = 600

        # create widgets 
        self.create_widgets()

    # create widgets method
    def create_widgets(self):
        # initial frame setup
        self.frame = tk.Frame(width=self.frame_width, height=self.frame_height, bg="black")

        # Cells grid
        self.canvas = tk.Canvas(self.frame,bg="purple", width=self.frame_width, height=500)

        # checkbutton state
        self.check_status = tk.BooleanVar()
        self.check_status.set(True)

        # Buttons
        self.display_checkbutton = tk.Checkbutton(self.frame, text="Display Grid", variable=self.check_status)
        self.play_button = tk.Button(self.frame, text="Start")
        self.pause_button = tk.Button(self.frame, text="Pause")
        self.next_button = tk.Button(self.frame, text="Next")
        self.clear_button = tk.Button(self.frame, text="Clear")

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

