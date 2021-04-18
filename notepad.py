# Import de la librairie Tkinter
import tkinter as tk
# Import des deux fonctions utilisés pour ouvrir et sauvegarder des fichiers
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Définition de la fonction create_bloc utilisé dans le main
def create_bloc():
    # Déclaration de choice
    choice = ''
    # Déclaration de curren_file qui va nous permettre
    # de savoir si un fichier est ouvert ou pas
    current_file = None
    # Création de la fenetre 
    window = tk.Tk()
    # Nouveau titre 
    window.title('Bloc Notes')
    # Taille de la fenetre
    width, height = 800, 500
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
    # éxécuter lors du clique du bouton Calculatrice dans le Menu Go To
    def calc():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal choice
        choice = 'calculator'
        # Détruire la fenetre Home
        window.destroy()

    # Définition de la fonction qui sera executé lors du clique 
    # du bouton New
    def new_note():
        # Lancer une nouvelle fenetre en appelant la fonction actuelle
        create_bloc() 
    # Définition de la fonction qui sera executé lors du clique 
    # du bouton Open
    def open_file():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal current_file
        # Ouvrir la fenetre de choix du fichier 
        # et récuperer le chemin du fichier désiré
        path = askopenfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        # Si le chemin d'un fichier à été récupérer
        if path:
            # Supprimer tout le contenu de l'éditeur
            editor.delete(1.0, tk.END)
            # Ouvrir le fichier en mode lecture se trouvant dans le chemin récupéré
            with open(path, 'r', encoding='utf8') as f:
                text = f.read() # Récuperer tout le contenu du fichier
                editor.insert(tk.END, text) # Mettre tout le contenu dans l'éditeur
            current_file = path # Modifier current_file afin de savoir qu'on à un fichier ouvert
            window.title('Bloc Notes - {}'.format(path)) # Modifier le titre de la fenetre
    # Définition de la fonction qui sera executé lors du clique 
    # du bouton Save
    def save_file():
        # Si aucun fichier n'est ouvert
        if current_file is None:
            # On sauvegarde sous
            save_file_as()
        # Sinon
        else:
            # On ouvre le fichier ouvert en mode écriture
            with open(current_file, 'w', encoding='utf8') as f:
                text = editor.get(1.0, tk.END) # Récupèrer tout le contenu de l'éditeur
                f.write(text) # Mettre le contenu récuperer dans le fichier
    # Définition de la fonction qui sera executé lors du clique 
    # du bouton Save As
    def save_file_as():
        # Rendre la variable choice nonlocal
        # Afin de pouvoir modifier sa valeur
        nonlocal current_file
        # Ouvrir la fenetre de choix du fichier 
        # et récuperer le chemin du fichier désiré
        path = asksaveasfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        # Si le chemin d'un fichier à été récupérer
        if path:
            # Ouvrir le fichier en mode écriture se trouvant dans le chemin récupéré
            with open(path, 'w', encoding='utf8') as f:
                text = editor.get(1.0, tk.END) # Récuprer tout le contenu de l'éditeur
                f.write(text) # Mettre ce contenu dans le fichier
            current_file = path # Modifier current_file afin de savoir qu'on à un fichier ouvert
            window.title('Bloc Notes - {}'.format(path)) # Modifier le titre de la fenetre
    # Définition de la fonction qui sera executé lors du clique 
    # du bouton Clear
    def clear_file():
        # Supprimer tout le contenu de l'éditeur
        editor.delete(1.0, tk.END)
    # Définition de la fonction qui sera executé lors du clique 
    # du bouton Exit
    def exit_file():
        # Détruire la fenetre
        window.destroy()

    # Création de la barre de menu
    menubar = tk.Menu(window)
    # Création du menu File
    file_menu = tk.Menu(window, tearoff=False)
    # Rajouter les boutons au menu File
    file_menu.add_command(label="New", command=new_note)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_file_as)
    file_menu.add_command(label="Clear", command=clear_file)
    file_menu.add_command(label="Exit", command=exit_file)
    # Création du menu Go To
    go_menu = tk.Menu(menubar, tearoff=False)
    # Rajouter les boutons au menu Go To
    go_menu.add_command(label="Home", command=home)
    go_menu.add_command(label="Calculatrice", command=calc)
    # Attacher les deux menus File et Go To a la barre de menu 
    menubar.add_cascade(menu=file_menu, label="File")
    menubar.add_cascade(menu=go_menu, label="Go To")
    # Attacher la barre de menu a la fenetre
    window.config(menu=menubar)

    # Créer le widget Text qui agira en tant qu'éditeur de texte
    editor = tk.Text(window)
    # Prendre la totalité de l'espace de la fenetre
    editor.pack(fill=tk.BOTH, expand=True)

    # Lancement de l'application
    done = window.mainloop()
    if done is None:
        # Une fois la fenetre détruite
        # On retourne la valeur de choice
        return choice