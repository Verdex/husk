
import struct

class Move:

    def __init__(self, direction):
        self.direction = direction

    def north():
        return Move(1)

    def east():
        return Move(2)

    def south():
        return Move(3)

    def west():
        return Move(4)

    def to_bytes(self):
        return struct.pack('!HB', 0x0001, self.direction)

    
