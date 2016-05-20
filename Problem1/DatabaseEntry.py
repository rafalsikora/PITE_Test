class DatabaseEntry:

    def __init__(self):
        self.data = {}
        return

    def Add(self, key, value):
        self.data[key] = value

    def string(self):
        return str(self.data)