from view import menu, show_contacts, print_message, input_contact
import model
from view import text

def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_succesfull)
            case 2:
                pass
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
        break
