import socket
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
key = ChaCha20Poly1305.generate_key()
with open('chacha20.key', 'wb') as key_file:
    key_file.write(key)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Server is on.....")
conn, addr = server_socket.accept()
print(f"Connection from {addr}")
while True:
    nonce = conn.recv(12)
    if not nonce:
        break
    encrypted_data = conn.recv(1024)
    if not encrypted_data:
        break
    chacha = ChaCha20Poly1305(key)
    try:
        decrypted_data = chacha.decrypt(nonce, encrypted_data, None)
        print(f"Message from {addr}: {decrypted_data.decode()}")
    except Exception as e:
        print(f"Decryption failed: {e}")
conn.close()
