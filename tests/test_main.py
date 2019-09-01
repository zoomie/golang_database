from home_encrypt import generate_key
from home_encrypt import encrypt
from home_encrypt import decrypt


def test_basic_encrypt():
    key = generate_key(5)
    msg_in = 'this coded message'
    cipher_msg = encrypt(msg_in, key)
    msg_out = decrypt(cipher_msg, key)
    assert msg_in == msg_out


def test_basic_encrypt_cipher_text():
    key = generate_key(5)
    msg_in = 'this coded message'
    cipher_msg = encrypt(msg_in, key)
    assert msg_in != cipher_msg
