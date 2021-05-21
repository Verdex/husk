
import struct

class Move:

    North = 1
    East = 2
    South = 3
    West = 4

    def __init__(self, direction):
        self.direction = direction

    def to_bytes(self):
        return struct.pack('!HB', 0x0001, self.direction)

    
