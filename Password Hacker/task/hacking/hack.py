import socket
import sys
import string
import itertools


def password_generator(index=1):
    characters = string.ascii_lowercase + string.digits
    while True:
        for password in itertools.product(characters, repeat=index):
            yield password
        index += 1


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
    main()
