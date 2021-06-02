
import struct
import socket

from comms.request import RequestPlayerId 

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
        self.port = None
        self.ip = None
        self.player_id = None

    def connect_to_server(self, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            output = create_request_packet([RequestPlayerId()], 0)
            s.sendall(output)
            #TODO wait for response that has player id
            #TODO if everything is okay, then we can set ip, port, and player_id
            self.ip = ip
            self.port = port
            self.player_id = 0
            #TODO need to return success or failiure for the console to communicate to the player

    def send_requests(self):
        requests = OutGoingRequests.output()
        if len(requests) == 0:
            return
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port)) 
            output = create_request_packet(requests, self.player_id)
            s.sendall(output)

def create_request_packet(requests, player_id):
    requests_bytes = [r.to_bytes() for r in requests]
    packet_length = 0
    for bs in requests_bytes:
        packet_length += len(bs)

    output = bytearray(struct.pack("!B", 0x00))         # packet version
    output.extend(struct.pack("!I", player_id))        
    output.extend(struct.pack("!I", packet_length))    

    for bs in requests_bytes:
        output.extend(bs)

    return output


OutGoingRequests = Requests()
GameServer = Server()