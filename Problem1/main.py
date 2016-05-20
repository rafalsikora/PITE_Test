from RecordBuilder import *
from DataWriter import *

database = RecordBuilder()

database.addRecord(name='Rafal', surname='Sikora', adress='Fieldorfa-Nila 200', age=24, heigh=180, salary=2000)
database.addRecord(name='Lukasz', surname='Lis', adress='Kukulskiego 23', age=33, heigh=201, salary=4000)
database.addRecord(name='Mariusz', surname='Kot', adress='Warszawska 4', age=56, heigh=143, salary=6000)
database.addRecord(name='Antoni', surname='Paderewski', adress='Popielata 2', age=12, heigh=120, salary=0)

exporter = DataWriter("databaseOutput.txt")
exporter.dump(database.content())