"""Hash functions"""

from __future__ import print_function

ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', \
            'm', 'n', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def url_hash(value):
    """Turn an integer hash into an alphanumeric string"""
    ret = ""
    while value:
        ret += ALPHABET[value % 32]
        value >>= 5
    return ret

if __name__ == '__main__':
    from random import randint
    print(len(ALPHABET))
    print([url_hash(randint(0, 8758863600785)) for _ in range(50)])
