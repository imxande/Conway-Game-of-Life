from tkinter import Menu, messagebox, Toplevel, Message, Button, PhotoImage, Scale, IntVar
import numpy as np

class AppMenu:
    def __init__(self, root, gui):
        self.root = root
        self.gui = gui

        # Setup menu
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
    
        # Create menu
        self.create_menu()

    def create_menu(self):
        """
        Creates view menu to display rules and 
        history of the game.
        """
        # Create menus
        view_menu = Menu(self.menu_bar, tearoff=0)
        preset_menu = Menu(self.menu_bar, tearoff=0)
        speed_menu = Menu(self.menu_bar, tearoff=0)

        # Add view menu to main menu bar
        self.menu_bar.add_cascade(label="View", menu=view_menu)
        self.menu_bar.add_cascade(label="Presets", menu=preset_menu)
        self.menu_bar.add_cascade(label="Speed", menu=speed_menu)

        # Add commands to menus
        view_menu.add_command(label="Rules", command=self.show_rules)
        view_menu.add_command(label="History", command=self.show_history)
        preset_menu.add_command(label="Choose Preset", command=self.show_presets)
        speed_menu.add_command(label="Adjust Speed", command=self.adjust_speed)

    def show_rules(self):
        """
        Displays game rules.
        """
        messagebox.showinfo(title="Game Rules", message="1- If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors.\n\n2-If the cell is dead, then it springs to life only in the case that it has 3 live neighbors.")

    def show_history(self):
        """
        Displays game history.
        """
        self.history_view = Toplevel(self.root)
        self.history_view.title("Game History")

        history_message = (
            "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.\n"
            "It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.\n"
            "One interacts with the Game of Life by creating an initial configuration and observing how it evolves.\n"
            "It is Turing complete and can simulate a universal constructor or any other Turing machine."
        )
        
        # display message
        message = Message(self.history_view, text=history_message, padx=20, pady=20)
        message.pack()

    def show_presets(self):
        """
        Displays the presets and associated button widgets and images in a toplevel window
        """
        self.preset_window = Toplevel(self.root)
        self.preset_window.title("Choose a preset")

        # Images
        self.glider_img = PhotoImage(file="./images/glider.png")
        self.heptomino_img = PhotoImage(file="./images/pi_heptomino.png")
        self.pentomino_img = PhotoImage(file="./images/r_pentomino.png")

        # Buttons
        glider_button = Button(self.preset_window, image=self.glider_img, command=self.gui.set_glider, cursor="hand2")
        glider_button.pack(padx=60, pady=10)
        heptomino_button = Button(self.preset_window, image=self.heptomino_img, command=self.gui.set_heptomino, cursor="hand2")
        heptomino_button.pack(padx=60, pady=10)
        pentomino_button = Button(self.preset_window, image=self.pentomino_img, command=self.gui.set_pentomino, cursor="hand2")
        pentomino_button.pack(padx=60, pady=10)


         
    def adjust_speed(self):
        """"Method that control the speed of next generations rendering"""
        self.speed_window = Toplevel(self.root)
        self.speed_window.title("Speed")
        var = IntVar()

        # Scales
        speed_scale = Scale(self.speed_window, variable=var, orient="horizontal", cursor="hand2", command=self._handle_scale_change, from_=100, to=500)
        speed_scale.set(self.gui.speed) # initial value of scale
        speed_scale.pack(padx=60, pady=10)


    def _handle_scale_change(self, val):
        """Method that handles what happens when scale changes"""
        slider_value = int(val)

        # speed ranges
        max_speed = 500
        min_speed = 100 

        # compute new_speed
        new_speed = int(min_speed + (slider_value - 100) *  (max_speed - min_speed) / 400)
        
        # update speed
        self.gui.set_speed(new_speed)
        
