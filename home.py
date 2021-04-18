# Import de la librarie Tkinter
import tkinter as tk
# Import de fonctions de la librarie Pillow
from PIL import ImageTk, Image

# Définition de la fonction create_home utilisé dans le main
def create_home():
    # Déclaration de choice
    choice = ''
    # Création de la fenetre 
    window = tk.Tk()
    # Nouveau titre 
    window.title('Home')
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

    # Chargement des images en utilisant Pillow
    bg_img = ImageTk.PhotoImage(
        Image.open('images/bg.jpg').resize( (width, height), Image.ANTIALIAS )
    )
    calc_img = ImageTk.PhotoImage(
        Image.open('images/calc.png').resize( (100, 100), Image.ANTIALIAS )
    )
    note_img = ImageTk.PhotoImage(
        Image.open('images/note.png').resize( (100, 100), Image.ANTIALIAS )
    )

    # Création d'un Label qui sera utilisé comme arrière plan
    # avec l'image selectionné
    bg_label = tk.Label(window, width=width, height=height, image=bg_img)
    # Affichage du Label en remplissant tout les espaces
    bg_label.pack(fill=tk.BOTH)
    # Création des deux boutons en utilisant les images
    calc_btn = tk.Button(window, width=100, height=100, image=calc_img, border=0, cursor='hand2', command=calculator)
    note_btn = tk.Button(window, width=100, height=100, image=note_img, border=0, cursor='hand2', command=note)
    # Positionnement des deux boutons
    # On utilise place et les attributs rel
    # pour placer les éléments relativement au parents 
    # qui est la fenetre, dans ce cas on centre les éléments
    calc_btn.place(relx=.5, rely=.3, anchor="center")
    note_btn.place(relx=.5, rely=.6, anchor="center")

    # Lancement de l'application
    done = window.mainloop()
    if done is None:
        # Une fois la fenetre détruite
        # On retourne la valeur de choice
        return choice 