from string import ascii_lowercase
from typing import Iterable

nums = range(len(ascii_lowercase) + 1)
letters = ascii_lowercase + ' '
letters_map = {char: num for char, num in zip(letters, nums)}
numbers_map = {num: char for char, num in zip(letters, nums)}


def generate_key() -> str:
    return '98765432'


def str_looper(string: str) -> Iterable[int]:
    while True:
        for char in string:
            yield int(char)


def mapping(char: str, num: int) -> str:
    in_num = letters_map[char]
    out_num = in_num + num
    if out_num > 27:
        out_num = out_num - 27
    return numbers_map[out_num]


def encrypt(msg: str, key: str) -> str:
    cipher_msg = ''
    for char, index in zip(msg, str_looper(key)):
        cipher_msg += mapping(char, index)
    return cipher_msg


def decrypt(msg: str, key: str) -> str:
    return msg
