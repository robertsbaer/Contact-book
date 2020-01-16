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
# rob = Contact(first_name='Robert', last_name='Baer', birthday=date(1986, 7, 3))
# rob.save()