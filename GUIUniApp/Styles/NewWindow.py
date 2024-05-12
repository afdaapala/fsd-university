import tkinter as tk
class NewWindow(tk.Toplevel):
  def __init__ (self, master, msg):
    super().__init__(master = master)
    self.title("Confirmation Window")
    self.geometry("400x150")
    self.configure(bg="#F5F5F5")
    self.resizable(False, False)

    label = tk.Label(self, text = msg, fg="#0f31db", bg="#F5F5F5",
                     font="Helvetica 16 bold")
    label.place(relx=0.5, rely=0.5, anchor="center")
    
