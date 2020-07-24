from cryptography.fernet import Fernet


def get_key(fd):
    with open(fd, "r") as f:
        fc = f.read()
    return fc.encode()


def encrypt(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as f:
        f_contents = f.read()

    encrypted = fer.encrypt(f_contents)

    with open(filename, "wb") as f:
        f.write(encrypted)


def decrypt(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as f:
        f_contents = f.read()

    decrypted = fer.decrypt(f_contents)

    with open(filename, "wb") as f:
        f.write(decrypted)

