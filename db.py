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
    birthday = DateField()

 
db.connect()
# db.drop_tables([Contact])
db.create_tables([Contact])
rob = Contact(first_name='Robert', last_name='Baer', birthday=date(1986, 7, 3))
rob.save()

def create_person():
    print("")
    full_name = input("First")

def update_person():
    #let the user input which last name they want to change
    last_name = input("Which last last name would you like to update? : ")
    #create an object that contains the possibility to find the last name 
    contact = Contact.get(Contact.last_name == last_name)
    #updates the object last_name with users imput
    contact.last_name = input("New last name: ")
    #saves to database
    contact.save()

def delete_person():
    last_name = str(input("Select by last name to delete that person: "))
    contact = Contact.get(Contact.last_name == last_name)
    contact.delete_instance()


# alex = Contact(first_name='Alex', last_name='Garcia', birthday=date(1986, 8, 20))
# alex.save()

# def callname():
#     contacts = Contact.select()
#     for contact in contacts:
#         print(contact.first_name, contact.last_name)
contacts = Contact.select()
for contact in contacts:
    print(contact.first_name, contact.last_name)


update_person()
delete_person()

contacts = Contact.select()
for contact in contacts:
    print(contact.first_name, contact.last_name)