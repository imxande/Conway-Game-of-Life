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
        # initial fram setup
        self.frame = tk.Frame(width=self.frame_width, height=self.frame_height, bg="purple")
        
        # show frame
        self.frame.pack()
