from home import create_home
from calculator import create_calculator
from notepad import create_note

choice = 'home'

while choice != '':
    if choice == 'home':
        choice = create_home()
    elif choice == 'calculator':
        choice = create_calculator()
    else:
        choice = create_note()