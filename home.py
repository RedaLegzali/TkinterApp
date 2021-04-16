import tkinter as tk
from PIL import ImageTk, Image

def create_home():
    choice = ''

    app = tk.Tk()
    width = 800
    height = 500
    geometry = f"{width}x{height}"
    app.geometry(geometry)
    app.resizable(0,0)
    app.title('Tkinter App')

    def calculator():
        nonlocal choice
        choice = 'calculator'
        app.destroy()
    def note():
        nonlocal choice
        choice = 'note'
        app.destroy()

    bg_img = ImageTk.PhotoImage(
        Image.open('images/bg.jpg').resize( (width, height), Image.ANTIALIAS )
    )
    calc_img = ImageTk.PhotoImage(
        Image.open('images/calc.png').resize( (100, 100), Image.ANTIALIAS )
    )
    note_img = ImageTk.PhotoImage(
        Image.open('images/note.png').resize( (100, 100), Image.ANTIALIAS )
    )

    bg_label = tk.Label(app, width=width, height=height, image=bg_img)
    bg_label.pack(fill=tk.BOTH)
    calc_btn = tk.Button(app, width=100, height=100, image=calc_img, border=0, cursor='hand2', command=calculator)
    note_btn = tk.Button(app, width=100, height=100, image=note_img, border=0, cursor='hand2', command=note)
    y = height // 2 - 100
    x = width // 2
    calc_btn.place(x=x-80, y=y)
    note_btn.place(x=x+50, y=y)

    done = app.mainloop()
    if done is None:
        return choice