import socket
import os

socket_path: str = "./uds_socket"

if os.path.exists(socket_path):
    os.remove(socket_path)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:

    server.bind(socket_path)
    server.listen(1)
    print("Service waiting for trigger from client.")

    while True:

        connection, _ = server.accept()
        with connection:

            data = connection.recv(1024)
            if not data: continue

            message = data.decode()
            print(f"Received trigger: {message}")
