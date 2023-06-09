from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def edit(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def add_phone(self, phone):
        if self.value is None:
            self.value = []
        self.value.append(phone)

    def remove_phone(self, phone):
        if self.value is not None and phone in self.value:
            self.value.remove(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phone()

    def add_phone(self, phone):
        self.phones.add_phone(phone)

    def remove_phone(self, phone):
        self.phones.remove_phone(phone)

    def edit_name(self, name):
        self.name.edit(name)

    def __str__(self):
        return f"Name: {self.name}\nPhones: {self.phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def search_records(self, search_term):
        results = []
        for record in self.data.values():
            if search_term.lower() in record.name.value.lower():
                results.append(record)
        return results


def hello_func():
    return 'How can I help you?'

def exit_func():
    return 'Good bye!'

def add_func(address_book):
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f'You added a new contact: {name}: {phone}.'

def change_func(address_book):
    name = input('Enter name: ')
    phone = input('Enter new phone: ')
    if name in address_book.data:
        record = address_book.data[name]
        record.remove_phone(record.phones.value)
        record.add_phone(phone)
        return f'You changed the number to {phone} for {name}.'
    return 'Use the add command, please.'

def show_func(address_book):
    contacts_list = ''
    for record in address_book.data.values():
        contacts_list += f'{record.name.value} : {record.phones} \n'
    return contacts_list

def main():
    address_book = AddressBook()

    COMMANDS = {
        'hello': hello_func,
        'exit': exit_func,
        'close': exit_func,
        'good bye': exit_func,
        'add': lambda: add_func(address_book),
        'change': lambda: change_func(address_book),
        'show all': lambda: show_func(address_book),
        # 'phone': lambda: search_func(address_book)
    }

    while True:
        command = input('Enter command: ').lower()
        if command == 'exit' or command == 'close' or command == 'good bye':
            print('Good bye!')
            break

        result = COMMANDS.get(command, lambda: 'Unknown command!')()
        print(result)

if __name__ == '__main__':
    main()
