from DatabaseEntry import *

class RecordBuilder:

    def __init__(self):
        self.listOfRecord = []

    def addRecord(self, **kwargs):
        entry = DatabaseEntry()
        for x in kwargs.keys():
            entry.Add(x, kwargs[x])
        self.listOfRecord.append(entry)

    def content(self):
        return self.listOfRecord