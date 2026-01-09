#!/usr/bin/env python3
import secrets
import string

PASSWORD_COUNT = 5
PASSWORD_LENGTH = 10

CHARSET = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits
)

def generate_password(length: int) -> str:
    return "".join(secrets.choice(CHARSET) for _ in range(length))

def main():
    for i in range(PASSWORD_COUNT):
        print(generate_password(PASSWORD_LENGTH))

if __name__ == "__main__":
    main()

