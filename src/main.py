from tkinter import Tk
from app.gui import AppGui


def main():
    # setup main application window
    root = Tk()

    # main window initial configurations
    root.wm_title("Conway\'s Game of Life")
    root.resizable(False, False)

    # initialize GUI app
    app = AppGui(master=root)


    # start application mainloop
    root.mainloop()

if __name__ == "__main__":
    main()


