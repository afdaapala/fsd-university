import tkinter as tk

class NewWindow(tk.Toplevel):
  def __init__ (self, master, msg):
    super().__init__(master = master)
    self.title("Confirmation Window")
    self.geometry("300x200")
    label = tk.Label(self, text = msg, fg="white", bg="#323232",
                     font="Helvetica 12 bold")
    # x = master.winfo_x()
    # y = master.winfo_y()
    # self.geometry("+%d+%d" %(x+300, y))
    self.configure(bg="#323232")
    self.resizable(False, False)
    label.place(relx=0.5, rely=-.3, anchor="center")
    label.pack()
