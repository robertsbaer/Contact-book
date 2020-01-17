# Import peewee
from peewee import *
from datetime import date
db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')
class BaseModel(Model):
    class Meta:
        database = db
class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()
    birthday = DateField()

 
db.connect()
# db.drop_tables([Contact])
db.create_tables([Contact])
# rob = Contact(first_name='Robert', last_name='Baer', phone_number='2022022020', birthday=date(1986, 7, 3))
# rob.save()

def welcome_page():
    print("What would you like do?" )
    print(' show contact: 1 \n create contact: 2 \n delete contact: 3 \n update contact: 4 \n exit: 5')
    answer = input('')
    if answer == '1':
        all_contact()
    elif answer == '2':
       create_person()
    elif answer == '3':
       delete_person()
    elif answer == '4':
       update_person()
    else:
       exit
       

def create_person():
    print("Create a new contact")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")
    birthday = input("Birthday: ")

    new_contact = Contact(first_name = first_name, last_name = last_name, phone_number = phone_number, birthday = birthday)

    new_contact.save()
    welcome_page()

def update_person():
    #let the user input which last name they want to change
    last_name = input("Which contact's last name would you like to update? : ")
    # first_name = input("Change or retype the first name: ")
    #create an object that contains the possibility to find the last name 
    contact = Contact.get(Contact.last_name == last_name)
    #updates the object last_name with users imput
    contact.last_name = input("New last name: ")
    contact.first_name = input("New first name: ")
    contact.phone_number = input("New Phone number: ")
    contact.birthday = input("New Birthday: ")
    # contact.first_name = input("first name")
    #saves to database
    contact.save()
    welcome_page()

def delete_person():
    last_name = str(input("Select by last name to delete that person: "))
    contact = Contact.get(Contact.last_name == last_name)
    contact.delete_instance()
    welcome_page()

def all_contact():
    contact = Contact.select()
    for contact in contact:
        print(contact.id, contact.first_name, contact.last_name, contact.phone_number, contact.birthday)
    welcome_page()

welcome_page()
