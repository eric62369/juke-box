from tkinter import *
from tkinter import filedialog, messagebox
from Application import App
import os

if __name__ == "__main__":
    # create the application
    root = Tk()
    root.title("qtMoJo")
    root.minsize(200, 100)
    # show an "Open" dialog box and return the path to the selected file
    playlist_path = "Jukebox Material"
    playlist_path = filedialog.askdirectory()
    if not isinstance(playlist_path, tuple):  # Avoid cancelled out case
        if os.path.exists(playlist_path):
            app = App(source=playlist_path, master=root)
            app.mainloop()
        else:
            messagebox.showerror("Given Directory Invalid",
                    "The given path for playlist source directory is not a valid path.")
    else:
        messagebox.showerror("No Selected Directory Path",
                "Please select a source directory for playlists to go to.")
