
class LocalId:

    def __init__(self, value):
        self.value = value

    def new(self):
        id = self.current 
        self.current += 1


