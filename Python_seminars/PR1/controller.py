from view import menu, show_contacts, print_message, input_contact, input_return
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
                word = input_search(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_search(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
            case 7:
                pass
            case 8:
                pass

