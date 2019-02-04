#!/usr/bin/env python3

import socket
import copy

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
HOST = '127.0.0.1'
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def get_data_from_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                return data.decode('utf-8') 
                # conn.sendall(data)
def get_data_from_file(counter):
    current_counter = 0
    linetoreturn = ""
    while True:
        with open("myfile.txt", "r") as f:
            for line in f:
                if line is None:
                    break
                if current_counter == counter:
                    linetoreturn = copy.deepcopy(line)
                    break
                current_counter += 1
        break
    return linetoreturn
        
