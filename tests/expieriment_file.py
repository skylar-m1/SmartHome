import tkinter

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg ="black")
frame.place(relwidth=1, relheight=1)

root.mainloop()
