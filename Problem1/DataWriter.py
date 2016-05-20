class DataWriter:

    def __init__(self, name):
        assert isinstance(name, str)
        self.fileName = name

    def dump(self, database):
        assert isinstance(database, list)
        file = open(self.fileName, 'w')
        for x in database:
            file.write(x.string()+"\n")
        file.close()