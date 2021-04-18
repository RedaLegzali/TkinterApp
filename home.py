# Import de la librarie Tkinter
import tkinter as tk 

# Définition de la fonction create_home utilisé dans le main
def create_home():
    # Déclaration de choice
    choice = ''
    # Création de la fenetre 
    window = tk.Tk()
    # Nouveau titre 
    window.title('Tkinter App')
    # Désactiver l'option de redimensionner la fenetre
    window.resizable(0,0)
    # Taille de la fenetre
    width, height = 800, 500
    size = "{}x{}".format(width, height)
    window.geometry(size)


    # Définition de la fonction qui sera 
    # éxécuter lors du clique du bouton Calculatrice
    def calculator():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal choice
        choice = 'calculator'
        # Détruire la fenetre Home
        window.destroy()
    # Définition de la fonction qui sera 
    # éxécuter lors du clique du bouton Bloc Notes
    def note():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal choice
        choice = 'note'
        # Détruire la fenetre Home
        window.destroy()

    # Création d'un label qui sera utilisé comme arrière plan
    bg_label = tk.Label(window, width=width, height=height, bg="#325288")
    # Positionnement du label
    bg_label.pack()

    # Création des deux boutons
    calc_button = tk.Button(
        bg_label,cursor="hand2", border=0, bg="#28b5b5", fg="#fff", padx=10, pady=10, text="Calculator", command=calculator
    )
    note_button = tk.Button(
        bg_label,cursor="hand2", border=0, bg="#8fd9a8", fg="#fff", padx=10, pady=10, text="Bloc Notes", command=note
    )
    # Positionnement des deux boutons
    # On utilise place et les attributs rel
    # pour placer les éléments relativement au parents 
    # qui est la fenetre, dans ce cas on centre les éléments
    calc_button.place(relx=.4, rely=.5, anchor="center")
    note_button.place(relx=.6, rely=.5, anchor="center")

    # Lancement de l'application
    done = window.mainloop()
    if done is None:
        # Une fois la fenetre détruite
        # On retourne la valeur de choice
        return choice
