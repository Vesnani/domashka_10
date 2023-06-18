from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_info(self):
        phones_info = ''

        for phone in self.phones:
            phones_info += f'{phone.value}, '
            return f'{self.name.value} : {phones_info[:-2]}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")

def hello_func():
    return 'Hello!'

def exit_func():
    return 'Goodbye!'

def add_record(address_book, name, phone):
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f'Record added: {name} - {phone}'

def change_func(address_book, name, new_phone):
    record = address_book.get_record(name)
    if record:
        record.change_phones([new_phone])
        return f'Phone number changed for {name}: {new_phone}'
    else:
        return f'Record not found for name: {name}'

def show_func(address_book):
    all_records = address_book.get_all_record()
    if all_records:
        return 'All records:\n' + '\n'.join([record.get_info() for record in all_records.values()])
    else:
        return 'No records found'


def main():
    address_book = AddressBook()

    COMMANDS = {
        'hello': hello_func,
        'exit': exit_func,
        'close': exit_func,
        'good bye': exit_func,
        'add': lambda: add_record(address_book, input('Enter name: '), input('Enter phone: ')),
        'change': lambda: change_func(address_book, input('Enter name you want to change: '),
                                      input('Enter new phone: ')),
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
