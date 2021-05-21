
import struct
import socket

from functools import reduce

from comms.request import Move  # TODO remove

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
            request = Move(Move.North)
            bs = request.to_bytes()
            z = bytearray(struct.pack("!B", 0x00))
            z.extend(struct.pack("!I", 0))
            z.extend(struct.pack("!I", len(bs)))
            z.extend(bs)
            x.sendall(z)

    def send_requests():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', port)) # TODO need to be able to set ip and port
            requests = OutGoingRequests.output() 
            requests_bytes = [r.to_bytes() for r in requests]
            packet_length = reduce( lambda a, b: len(a) + len(b), requests_bytes ) # TODO does this work

            output = bytearray(struct.pack("!B", 0x00))         # packet version
            output.extend(struct.pack("!I", 0))                 # TODO player id
            output.extend(struct.pack("!I", packet_length)))    # packet length

            for bs in requests_bytes:
                output.extend(bs)

            s.sendall(output)


OutGoingRequests = Requests()
GameServer = Server()