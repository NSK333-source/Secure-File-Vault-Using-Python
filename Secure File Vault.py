from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import os

BLOCK_SIZE = 16

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_file(file_path, password):
    key = get_key(password)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = iv + cipher.encrypt(pad(data))
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_data)
    os.remove(file_path)
    print("File encrypted successfully.")

def decrypt_file(file_path, password):
    key = get_key(password)

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data[BLOCK_SIZE:]))
        original_name = file_path.replace('.enc', '')
        with open(original_name, 'wb') as f:
            f.write(decrypted_data)
        os.remove(file_path)
        print("File decrypted successfully.")
    except:
        print("Decryption failed. Wrong password or corrupted file.")

def main():
    print("1. Encrypt File")
    print("2. Decrypt File")
    choice = input("Choose (1/2): ")
    file_path = input("Enter file path: ")
    password = input("Enter password: ")

    if choice == '1':
        encrypt_file(file_path, password)
    elif choice == '2':
        decrypt_file(file_path, password)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
