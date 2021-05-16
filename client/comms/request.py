
import struct

class Move:

    def __init__(self, direction):
        self.direction = direction

    def to_bytes(self):
        return struct.pack('!HH')
        
    
