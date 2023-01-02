import socket
import sys
import string
import itertools


def main():
    ip_address, port = sys.argv[1:]
    with socket.socket() as conn:
        conn.connect((ip_address, int(port)))
        n = 1
        wrong_password = True
        while wrong_password:
            characters = string.ascii_lowercase + string.digits
            for message in itertools.product(characters, repeat=n):
                conn.send(''.join(message).encode())
                response = conn.recv(1024)
                if response.decode() == 'Connection success!':
                    wrong_password = False
                    print(''.join(message))
                    break
            n += 1


if __name__ == "__main__":
    main()
