from string import ascii_lowercase
from random import randint
from typing import Iterable


nums = range(1, len(ascii_lowercase) + 2)
letters = ascii_lowercase + ' '
letters_map = {char: num for char, num in zip(letters, nums)}
numbers_map = {num: char for char, num in zip(letters, nums)}


def generate_key(length: int) -> str:
    key = ''
    for num in range(length):
        key += str(randint(0, 10))
    return key


def str_looper(string: str) -> Iterable[int]:
    while True:
        for char in string:
            yield int(char)


def mapping_encrypt(char: str, num: int) -> str:
    in_num = letters_map[char]
    out_num = in_num + num
    if out_num > 27:
        out_num = out_num - 27
    return numbers_map[out_num]


def encrypt(msg: str, key: str) -> str:
    cipher_msg = ''
    for char, index in zip(msg, str_looper(key)):
        cipher_msg += mapping_encrypt(char, index)
    return cipher_msg


def mapping_decrypt(char: str, num: int) -> str:
    in_num = letters_map[char]
    out_num = in_num - num
    if out_num < 1:
        out_num = out_num + 27
    return numbers_map[out_num]


def decrypt(cipher_msg: str, key: str) -> str:
    msg = ''
    for char, index in zip(cipher_msg, str_looper(key)):
        msg += mapping_decrypt(char, index)
    return msg
