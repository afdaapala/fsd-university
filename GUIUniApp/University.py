import tkinter as tk
from tkinter import *
from Models.Student import StudentGUI

class UniversityGUI:
    def main(self):
      root = tk.Tk()
      student = StudentGUI

      root.geometry("500x200")
      root.title("Student System")
      root.configure(bg="#323232")
      root.resizable(False, False)

      label = tk.Label(root, text="Welcome to Student System",
                      fg="white", font="Helvetica 18 bold",
                      padx=20, pady=20)
      label.pack()

      btn = tk.Button(root, text="A(dmin)", font='Helvetica 14 bold')
      btn.pack()

      btn = tk.Button(root, text="S(tudent)", font='Helvetica 14 bold', command=student.viewMenu)
      btn.pack()

      btn = tk.Button(root, text="X(exit)", font='Helvetica 14 bold', command=lambda: root.quit())
      btn.pack()

      root.mainloop()

if __name__ == "__main__":
    univ = UniversityGUI()
    univ.main()
