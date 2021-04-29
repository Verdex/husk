
class Id:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1
        return self.value

class Database:
    def __init__(self, name):
        self.name = name
        self.counter = Counter()
        self.data = {}

    def add(self, item):
        value = self.counter.inc()
        item.id = Id(self.name, value)
        self.data[value] = item
        return item.id

    def remove(self, id):
        assert id.name == self.name
        if id.value in self.data:
            del self.data[id.value]

    def get(self, id):
        assert id.name == self.name
        if id.value in self.data:
            return self.data[id.value]
        else:
            return False

    def all(self):
        return self.data.values()

Surfaces = Database("Surfaces")
MobFieldObjects = Database("MobFieldObjects")