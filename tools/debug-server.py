#!/bin/env python3
# Example of simple echo server
# www.solusipse.net

import socket

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 22447))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        print(current_connection);
        while True:
            try:
                data = current_connection.recv(2048)
            except:
                print('connection closed')
                break

            if data == 'quit\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                break

            elif data == 'stop\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                exit()

            elif data:
                current_connection.send(data)
                print(data)


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
