from view import menu
import model

def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
