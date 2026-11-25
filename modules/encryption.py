from chacha20poly1305 import ChaCha20Poly1305
import ecdsa
from hashlib import sha256
import hmac
from os import urandom

# CONSTANTS
CURVE = ecdsa.SECP256k1 # y^2 = x^3 - 7
CONNECTION_SALT='client-server'.encode() # common string to salt key generation

with open("encryption\\server_public_key.txt") as file:
    SERVER_PUBLIC_KEY = file.readline()

SERVER_PUBLIC_KEY = bytes.fromhex(SERVER_PUBLIC_KEY)
SERVER_PUBLIC_KEY = ecdsa.VerifyingKey.from_string(SERVER_PUBLIC_KEY, curve=CURVE)

def generate_new_keys():
    """
    A function to generate a new pair of encryption keys for this session
    """
    client_private = ecdsa.SigningKey.generate(CURVE)
    client_public = client_private.verifying_key
    return client_private, client_public

def verify_server(signature, client_public_key, server_public_key):
    """
    A procedure to verify the server - will raise BadSignatureError if verification fails
    """
    both_keys = key_to_string(client_public_key) + key_to_string(server_public_key) # concatenates the public keys
    SERVER_PUBLIC_KEY.verify(signature, both_keys) # returns True if the verification passes, and throws an error if it fails

def compute_shared_key(client_private_key, server_public_key):
    """
    A function which computes the shared key (should be identical to the server key)
    """
    client_ecdh = ecdsa.ECDH(CURVE, client_private_key, server_public_key)
    client_secret = client_ecdh.generate_sharedsecret_bytes()
    client_key = hmac.new(CONNECTION_SALT, client_secret, sha256).digest()
    return client_key

def generate_cipher(client_private_key, server_public_key):
    """
    A function which uses the shared key to calculate the encryption cipher (identical to server cipher)
    """
    encryption_key = compute_shared_key(client_private_key, server_public_key)
    encryption_cipher = ChaCha20Poly1305(encryption_key)
    return encryption_cipher

def encrypt_message(message_bytes, encryption_cipher):
    """
    A function to encrypt messages using the encryption cipher
    Takes the message in bytes and the cipher to use as parameters
    Returns the encrypted message
    """
    n_once = urandom(12)  # always different random for each message sent
    encrypted_message = encryption_cipher.encrypt(n_once, message_bytes)
    encrypted_message = n_once + encrypted_message
    return encrypted_message

def decrypt_message(encrypted_message, encryption_cipher):
    """
    A function to decrypt messages using the encryption cipher
    Takes an encrypted message and the cipher used as parameters
    Returns the decrypted message in bytes
    """
    n_once = encrypted_message[:12]
    message = encrypted_message[12:]
    message_bytes = encryption_cipher.decrypt(n_once, message)
    return message_bytes

def key_to_string(key):
    """
    A function to convert a VerifyingKey object to a string
    """
    return key.to_string()

def string_to_key(key_string):
    """
    A function to convert a string into a VerifyingKey object
    """
    return ecdsa.VerifyingKey.from_string(key_string, curve=CURVE)

def generate_hashed_password(password, salt):
    return str(sha256((password + salt).encode()).hexdigest())