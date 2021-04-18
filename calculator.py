# Import de la librarie Tkinter
import tkinter as tk

# Définition de la fonction create_calc utilisé dans le main
def create_calc():
    # Déclaration de choice
    choice = ''
    # Création de la fenetre 
    window = tk.Tk()
    # Nouveau titre 
    window.title('Calculator')
    # Désactiver l'option de redimensionner la fenetre
    window.resizable(0,0)
    # Taille de la fenetre
    width, height = 300, 325
    size = "{}x{}".format(width, height)
    window.geometry(size)

    # Définition de la fonction qui sera 
    # éxécuter lors du clique du bouton Home dans le Menu Go To
    def home():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal choice
        choice = 'home'
        # Détruire la fenetre Home
        window.destroy()
    # Définition de la fonction qui sera 
    # éxécuter lors du clique du bouton Bloc Notes dans le Menu Go To
    def note():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal choice
        choice = 'note'
        # Détruire la fenetre Home
        window.destroy()

    # Création de la barre de menu
    menubar = tk.Menu(window)
    # Création du menu Go To
    menu = tk.Menu(menubar, tearoff=False)
    # Rajouter les boutons au menu Go To
    menu.add_command(label='Home', command=home)
    menu.add_command(label='Bloc Notes', command=note)
    # Attacher le menu Go To a la barre de menu
    menubar.add_cascade(menu=menu, label='Go To')
    # Attacher la barre de menu a la fenetre
    window.config(menu=menubar)

    # Création de la frame qui va contenir 
    entry_frame = tk.Frame(window, width=width, height=50, border=0)
    # Positionnement de la frame en haut de la fenetre
    entry_frame.pack(side=tk.TOP)

    # Création de la fonction qui sera executé lorsqu'un bouton sera appuyé
    # En passant un parametre 
    def keyPress(key):
        # On récupère le paramètre passé à la fonction 
        # et on le stock dans la variable key
        if key == 'clear':
            # Si key est égale à clear alors on efface le contenu de equation
            equation.set('')
        elif key == 'erase':
            # Si key est égale à erase alors on efface le dernier element de equation
            # Dans ce cas on utilise le slicing de Python
            value = equation.get()
            equation.set( value[0:-1] )
        elif key == '=':
            # Si key est égal à = on evalue l'expression contenu dans équation afin d'avoir le résultat
            value = equation.get()
            result = eval(value)
            equation.set(result)
        else:
            # Si on appuie sur un autre bouton à part ces derniers 
            # On concatène la valeur de ce bouton avec ce qui est deja contenu dans equation
            value = equation.get()
            equation.set(value + key)

    # Initialisation de la variable qui va contenir la chaine de caractère
    # du widget Entry
    equation = tk.StringVar()
    # Création du widget Entry dans la frame entry_frame
    entry = tk.Entry(entry_frame, font=('arial', 18, 'bold'), textvariable=equation, width=width, bg="#fff", border=0, justify=tk.RIGHT)
    # Positionnement de l'élément 
    entry.grid(row=0, column=0)
    entry.pack(ipady=10)

    # Création de la frame qui contiendra tout les boutons
    btn_frame = tk.Frame(window, width=width, height=height, bg="grey")
    btn_frame.pack()
    # Couleur des boutons
    btn_color = "#f8f5f1"
    # Création des boutons en les positionnants via le Grid
    # On utlise une fonction lambda pour appeler la fonction keyPress et lui passer un paramètre
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

    # Lancement de l'application
    done = window.mainloop()
    if done is None:
        # Une fois la fenetre détruite
        # On retourne la valeur de choice
        return choice