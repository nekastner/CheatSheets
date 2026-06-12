import socket

socket_path: str = './uds_socket'

try:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(socket_path)
        client.sendall(b"START_TASK")
        print("Send trigger to service via socket.")

except FileNotFoundError:
    print("Service not active (no socket found).")