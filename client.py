import socket
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import time
with open('chacha20.key', 'rb') as key_file:
    key = key_file.read()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
while True:
    message = input("Enter a message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    encrypted_message = chacha.encrypt(nonce, message.encode(), None)
    client_socket.sendall(nonce + encrypted_message)
    print(f"Sent (encrypted): {encrypted_message.hex()}")
client_socket.close()