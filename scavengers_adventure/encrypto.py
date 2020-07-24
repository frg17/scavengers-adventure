from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(data, key):
    processed_key = pad(key.encode(), 32)[0:32]
    cipher = AES.new(processed_key, AES.MODE_CTR, nonce=b"")

    encrypted_bytes = cipher.encrypt(data)

    return encrypted_bytes


def decrypt(data, key):
    processed_key = pad(key.encode(), 32)[0:32]
    cipher = AES.new(processed_key, AES.MODE_CTR, nonce=b"")

    decrypted_bytes = cipher.decrypt(data)

    return decrypted_bytes


def encrypt_file(filename, key):
    with open(filename, "rb") as f:
        encrypted_data = encrypt(f.read(), key)
    
    return encrypted_data


def decrypt_file(filename, key):
    with open(filename, "rb") as f:
        decrypted_data = decrypt(f.read(), key)
    
    return decrypted_data


def save_to(filename, content):
    with open(filename, "wb") as f:
        f.write(content)


def encrypt_save(infile, outfile, key):
    dat = encrypt_file(infile, key)
    save_to(outfile, dat)
    

def decrypt_save(infile, outfile, key):
    dat = decrypt_file(infile, key)
    save_to(outfile, dat)
    