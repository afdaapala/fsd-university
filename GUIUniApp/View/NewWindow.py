import tkinter as tk
from Styles.Style import Colors
class NewWindow(tk.Toplevel):
  def __init__ (self, master, msg):
    super().__init__(master = master)
    self.title("Confirmation Window")
    self.geometry("400x150")
    self.configure(bg=Colors.windowBgColor)
    self.resizable(False, False)

    label = tk.Label(self, text = msg, fg=Colors.windowTextColor, bg=Colors.windowBgColor,
                     font="Helvetica 16 bold")
    label.place(relx=0.5, rely=0.5, anchor="center")
    
