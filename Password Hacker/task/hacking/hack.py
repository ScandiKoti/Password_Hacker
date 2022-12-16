import socket
import sys


def main():
    ip_address, port, message = sys.argv[1:]
    with socket.socket() as conn:
        conn.connect((ip_address, int(port)))
        conn.send(message.encode())
        response = conn.recv(1024)
        print(response.decode())


if __name__ == "__main__":
    main()
