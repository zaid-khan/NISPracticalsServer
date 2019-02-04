#!/usr/bin/env python3

import socket

#HOST = '127.0.0.1'  # The server's hostname or IP address
def send_data_to_server(my_str):
    HOST = '172.18.36.116'
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(my_str.encode('utf-8'))
        data = s.recv(1024)

    print('Received', repr(data))
