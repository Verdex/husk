
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



