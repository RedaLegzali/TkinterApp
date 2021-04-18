# Import de la librairie tkinter avec un alias : tk 
import tkinter as tk
# Import des fonctions
from home import create_home
from calculator import create_calc
from notepad import create_bloc

# On commence avec home
choice = 'home'
# Tant que le choix n'est pas vide on lance une fenetre
# Home ou Calculatrice ou Bloc Notes
while choice != '':
    if choice == 'home':
        choice = create_home()
    elif choice == 'note':
        choice = create_bloc()
    elif choice  == 'calculator':
        choice = create_calc()

# Fin du programme