import random
import string
import sys

def generate_password(length):
    if length < 3:
        raise ValueError("Password length must be at least 3 to include all character types.")

    characters = string.ascii_letters + string.digits
    password = []

    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))

    for _ in range(length - 3):
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [length]")
        sys.exit(1)

    length = int(sys.argv[1])
    print(generate_password(length))
