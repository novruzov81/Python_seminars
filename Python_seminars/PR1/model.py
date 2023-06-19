phone_book = []
path = 'phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readline()
    for contact in data:
        name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'name': name, 'phone': phone, 'comment': comment})