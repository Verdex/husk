
import struct
import socket
from functools import reduce

class Requests:
    def __init__(self):
        self.rs = []

    def add(self, request):
        self.rs.append(request)

    def output(self):
        x = self.rs
        self.rs = []
        return x

class Server:

    def __init__(self):
        pass

    def test(self, port):
        print(f"PORT {port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
            x.connect(('127.0.0.1', port))
            z = bytearray(struct.pack("!HH", 0xAAFF, 0xEECC))
            z.extend(struct.pack('!H', 0x1234))
            x.sendall(z)

    def send_requests():
        pass
        #rs = OutGoingRequests.output()
        #struct.pack('!')




OutGoingRequests = Requests()
GameServer = Server()