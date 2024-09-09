from tkinter import Tk


def main():
    # setup main application window
    root = Tk()

    # main window initial configurations
    root.geometry("600x600")
    root.wm_title("Conway\'s Game of Life")


    # start application mainloop
    root.mainloop()

if __name__ == "__main__":
    main()


