import tkinter as tk

def create_calculator():
    choice = ''

    app = tk.Tk()
    width = 300
    height = 325
    geometry = f"{width}x{height}"
    app.geometry(geometry)
    app.resizable(0,0)
    app.title('Calculator')

    def home():
        nonlocal choice
        choice = 'home'
        app.destroy()
    def note():
        nonlocal choice
        choice = 'note'
        app.destroy()

    menubar = tk.Menu(app)
    menu = tk.Menu(menubar, tearoff=False)
    menu.add_command(label='Home', command=home)
    menu.add_command(label='Bloc Notes', command=note)
    menubar.add_cascade(menu=menu, label='Go To')
    app.config(menu=menubar)

    entry_frame = tk.Frame(app, width=width, height=50, border=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    entry_frame.pack(side=tk.TOP)

    def keyPress(key):
        if key == 'clear':
            equation.set('')
        elif key == 'erase':
            value = equation.get()
            equation.set( value[0:-1] )
        elif key == '=':
            value = equation.get()
            result = eval(value)
            equation.set(result)
        else:
            value = equation.get()
            equation.set(value + key)

    equation = tk.StringVar()
    entry = tk.Entry(entry_frame, font=('arial', 18, 'bold'), textvariable=equation, width=width, bg="#fff", border=0, justify=tk.RIGHT)
    entry.grid(row=0, column=0)
    entry.pack(ipady=10)

    btn_frame = tk.Frame(app, width=width, height=height, bg="grey")
    btn_frame.pack()
    btn_color = "#f8f5f1"
    tk.Button(btn_frame, text="Clear", fg="black", width=21, height=3, border=0, bg="#fff", cursor="hand2", command=lambda: keyPress('clear')).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
    tk.Button(btn_frame, text="Erase", fg="black", width=10, height=3, border=0, bg="#fff", cursor="hand2", command=lambda: keyPress('erase')).grid(row=0, column=2, padx=1, pady=1)
    tk.Button(btn_frame, text="/", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('/')).grid(row=0, column=3, padx=1, pady=1)
    tk.Button(btn_frame, text="7", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('7')).grid(row=1, column=0, padx=1, pady=1)
    tk.Button(btn_frame, text="8", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('8')).grid(row=1, column=1, padx=1, pady=1)
    tk.Button(btn_frame, text="9", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('9')).grid(row=1, column=2, padx=1, pady=1)
    tk.Button(btn_frame, text="x", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('*')).grid(row=1, column=3, padx=1, pady=1)
    tk.Button(btn_frame, text="4", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('4')).grid(row=2, column=0, padx=1, pady=1)
    tk.Button(btn_frame, text="5", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('5')).grid(row=2, column=1, padx=1, pady=1)
    tk.Button(btn_frame, text="6", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('6')).grid(row=2, column=2, padx=1, pady=1)
    tk.Button(btn_frame, text="-", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('-')).grid(row=2, column=3, padx=1, pady=1)
    tk.Button(btn_frame, text="1", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('1')).grid(row=3, column=0, padx=1, pady=1)
    tk.Button(btn_frame, text="2", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('2')).grid(row=3, column=1, padx=1, pady=1)
    tk.Button(btn_frame, text="3", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('3')).grid(row=3, column=2, padx=1, pady=1)
    tk.Button(btn_frame, text="+", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('+')).grid(row=3, column=3, padx=1, pady=1)
    tk.Button(btn_frame, text="0", fg="black", width=21, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('0')).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
    tk.Button(btn_frame, text=".", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('.')).grid(row=4, column=2, padx=1, pady=1)
    tk.Button(btn_frame, text="=", fg="black", width=10, height=3, border=0, bg=btn_color, cursor="hand2", command=lambda: keyPress('=')).grid(row=4, column=3, padx=1, pady=1)


    done = app.mainloop()
    if done is None:
        return choice