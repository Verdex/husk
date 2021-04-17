
class LocalIdManager:

    def __init__(self):
        self.current = 1

    def new(self):
        id = LocalId(self.current)
        self.current += 1
        return id

class LocalId:

    def __init__(self, value):
        self.value = value


class LocalDatabase:

    def __init__(self, id_manager):
        self.data = {}
        self.id_manager = id_manager 

    def add(self, item):
        id = self.id_manager.new()
        item.id = id
        self.data[id.value] = item
        return id

    def remove(self, id):
        assert type(id) == LocalId, "Encountered non-local id in local database remove"
        if id.value in item:
            del item[id.value]

    def get(self, id):
        assert type(id) == LocalId, "Encountered non-local id in local database get"
        return self.data[id.value]
        

def init_local_database():
    return LocalDatabase(LocalIdManager())