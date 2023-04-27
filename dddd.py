import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Рисуем прямую
canvas.create_line(0, 150, 60, 150)

root.mainloop()