from tkinter import Menu, messagebox

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
        # Create a View menu
        view_menu = Menu(self.menu_bar, tearoff=0)

        # Add view menu to main menu bar
        self.menu_bar.add_cascade(label="View", menu=view_menu)

        # Add commands to view menu
        view_menu.add_command(label="Rules", command=self.show_rules)
        view_menu.add_command(label="History", command=self.show_history)

    def show_rules(self):
        """
        Displays game rules.
        """
        messagebox.showinfo(title="Game Rules", message="Game rules go here.")

    def show_history(self):
        """
        Displays game history.
        """ 
        messagebox.showinfo(title="Game History", message="History goes here.")

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
        # Create a View menu
        view_menu = Menu(self.menu_bar, tearoff=0)

        # Add view menu to main menu bar
        self.menu_bar.add_cascade(label="View", menu=view_menu)

        # Add commands to view menu
        view_menu.add_command(label="Rules", command=self.show_rules)
        view_menu.add_command(label="History", command=self.show_history)

    def show_rules(self):
        """
        Displays game rules.
        """
        messagebox.showinfo(title="Game Rules", message="Game rules go here.")

    def show_history(self):
        """
        Displays game history.
        """ 
        messagebox.showinfo(title="Game History", message="History goes here.")

