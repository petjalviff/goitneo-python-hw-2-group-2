class Field:
    def __init__(self, value):
        self.value = value    
    
    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) < 10 or len(value) > 13:
            raise ValueError("Phone number must be a 10-digit number.")
        super().__init__(value)
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []    
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))    
        
    def delete_phone(self, phone):
        temp_list=[]
        for i in self.phones:
            if i.value != phone:
                temp_list.append(i.value)
        self.phones=temp_list
        print("phone -",phone,"is deleted in contact -", self.name)

    
    def change_phone(self, phone_old, phone_new):
        self.delete_phone(phone_old)
        self.add_phone(phone_new)
        print("phone changed in contact -", self.name)    
    
    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None    
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"



class AddressBook:
    def __init__(self):
        self.data = {}    
    
    def add_record(self, record):
        self.data[record.name.value] = record    

    def delete(self, name):
        if name in self.data:
            del self.data[name]    
    
    def find(self, name):
        return self.data.get(name)    
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())



contact1=Record("Andrii")
contact2=Record("Igor")

ad_book=AddressBook()
ad_book.add_record(contact1)
ad_book.add_record(contact2)
print(ad_book)
print("")

contact2.add_phone("77777777778")
contact1.add_phone("1234567980")
contact1.add_phone("555555555567")
contact1.add_phone("6666666666678")
contact1.add_phone("8888888888678")
contact1.add_phone("9999999999111")
contact2.change_phone("7777777777","380989515265")

print(ad_book)
contact1.delete_phone("5555555555")

print("")
print("Adress Book:", ad_book)
print("")
print(contact1)

