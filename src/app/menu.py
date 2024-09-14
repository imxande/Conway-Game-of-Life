from tkinter import Menu, messagebox, Toplevel, Message

class AppMenu:
    def __init__(self, root):
        self.root = root

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

        # Add view menu to main menu bar
        self.menu_bar.add_cascade(label="View", menu=view_menu)
        self.menu_bar.add_cascade(label="Presets", menu=preset_menu)

        # Add commands to menus
        view_menu.add_command(label="Rules", command=self.show_rules)
        view_menu.add_command(label="History", command=self.show_history)
        preset_menu.add_command(label="Pick")

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


