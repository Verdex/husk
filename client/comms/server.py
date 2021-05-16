
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

    def send_requests():
        rs = OutGoingRequests.output()




OutGoingRequests = Requests()
GameServer = Server()