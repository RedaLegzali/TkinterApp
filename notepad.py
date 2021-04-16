import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font

def create_note():
    choice = ''
    current_file = None

    app = tk.Tk()
    width = 800
    height = 500
    geometry = f"{width}x{height}"
    app.geometry(geometry)
    app.title('Bloc Notes')

    def home():
        nonlocal choice
        choice = 'home'
        app.destroy()
    def calculator():
        nonlocal choice
        choice = 'calculator'
        app.destroy()

    def open_file():
        nonlocal current_file
        path = askopenfilename( 
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")] 
        )
        if path:
            editor.delete(1.0, tk.END)
            with open(path, 'r') as f:
                text = f.read()
                editor.insert(tk.END, text)
            current_file = path
            app.title(f'Bloc Notes - {path}')
    def save_as():
        nonlocal current_file
        path = asksaveasfilename( 
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")] 
        )
        if path:
            with open(path, 'w') as f:
                text = editor.get(1.0, tk.END)
                text = f.write(text)
            current_file = path
            app.title(f'Bloc Notes - {path}')
    def save_file():
        if current_file is None:
            save_as()
        else:
            with open(current_file, 'w') as f:
                text = editor.get(1.0, tk.END)
                text = f.write(text)

    def copy():
        try:
            value = editor.selection_get()
            app.clipboard_clear()
            app.clipboard_append(value)
        except Exception:
            pass
    def paste():
        value = app.clipboard_get()
        editor.insert(tk.INSERT, value)

    def regular():
        reg_font = font.Font(weight="normal")
        editor.config(font=reg_font)
    def bold():
        bold_font = font.Font(weight="bold")
        editor.config(font=bold_font)
    def italic():
        italic_font = font.Font(slant="italic")
        editor.config(font=italic_font)
    def roman():
        roman_font = font.Font(slant="roman")
        editor.config(font=roman_font)


    menubar = tk.Menu(app)
    file_menu = tk.Menu(menubar, tearoff=False)
    file_menu.add_command(label='New', command=lambda: create_note())
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_file)
    file_menu.add_command(label='Save As', command=save_as)
    file_menu.add_command(label='Clear', command=lambda: editor.delete(1.0, tk.END))
    file_menu.add_command(label='Exit', command=lambda: app.destroy())

    edit_menu = tk.Menu(menubar, tearoff=False)
    edit_menu.add_command(label='Copy', command=copy)
    edit_menu.add_command(label='Paste', command=paste)

    format_menu = tk.Menu(menubar, tearoff=False)
    format_menu.add_command(label='Regular', command=regular)
    format_menu.add_command(label='Bold', command=bold)
    format_menu.add_command(label='Italic', command=italic)
    format_menu.add_command(label='Roman', command=roman)

    go_menu = tk.Menu(menubar, tearoff=False)
    go_menu.add_command(label='Home', command=home)
    go_menu.add_command(label='Calculatrice', command=calculator)

    menubar.add_cascade(menu=file_menu, label='File')
    menubar.add_cascade(menu=edit_menu, label='Edit')
    menubar.add_cascade(menu=format_menu, label='Format')
    menubar.add_cascade(menu=go_menu, label='Go To')
    app.config(menu=menubar)

    editor = tk.Text(app)
    editor.pack(fill=tk.BOTH, expand=True)

    done = app.mainloop()
    if done is None:
        return choice