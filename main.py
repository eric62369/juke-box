import tkinter as tk
from application import App

if __name__ == "__main__":
    # create the application
    root = tk.Tk()
    root.title("qtMoJo")
    root.minsize(200, 100)

    app = App(master=root)
    app.mainloop()
