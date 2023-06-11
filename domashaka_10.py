class Field:
    def __init__(self, value=None):
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
        self.phones = [Phone()]

    def add_phone(self, phone):
        for phone_index in self.phones:
            phone_index.add_phone(phone)

    def remove_phone(self, phone):
        for phone_index in self.phones:
            phone_index.remove_phone(phone)

    def edit_name(self, name):
        self.name.edit(name)

    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones[0].value)
        return f"Name: {self.name}\nPhones: {phone_numbers}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        if record.name.value in self.data:
            existing_record = self.data[record.name.value]
            existing_record.add_phone(record.phones[0].value[0])
        else:
            self.data[record.name.value] = record

    def delete_record(self, name):
        if name in self.data:
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


def add_func(address_book, name, phone):
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f'You added a new contact: {name}: {phone}.'


def change_func(address_book, name, phone):
    if name in address_book.data:
        record = address_book.data[name]
        record.phones[0].value = [phone]  # Замінюємо список номерів на новий список з одним номером
        return f'You changed the number to {phone} for {name}.'
    return 'Use the add command, please.'


def show_func(address_book):
    contacts_list = ''
    for record in address_book.data.values():
        phone_numbers = ', '.join(str(phone) for phone in record.phones[0].value)
        contacts_list += f'{record.name.value} : [{phone_numbers}]\n'
    return contacts_list


def main():
    address_book = AddressBook()

    COMMANDS = {
        'hello': hello_func,
        'exit': exit_func,
        'close': exit_func,
        'good bye': exit_func,
        'add': lambda: add_func(address_book, input('Enter name: '), input('Enter phone: ')),
        'change': lambda: change_func(address_book, input('Enter name you want to change: '), input('Enter new phone: ')),
        'show all': lambda: show_func(address_book),
    }

    while True:
        command = input('Enter command: ').lower()
        if command in ('exit', 'close', 'good bye'):
            print('Good bye!')
            break

        result = COMMANDS.get(command, lambda: 'Unknown command!')()
        print(result)


if __name__ == '__main__':
    main()
