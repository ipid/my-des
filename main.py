from my_des import *
from rich import print
from rich.text import Text
from rich.panel import Panel


def main():
    print(Panel(Text('Welcome to use my DES encryptor!', 'bold green', justify='center')))
    print('[cyan b]Plaintext: [/]', end='')
    plaintext = input()

    print('[cyan b]Key: [/]', end='')
    key = input()

    plaintext, key = bytes.fromhex(plaintext), bytes.fromhex(key)
    if len(plaintext) != 8 or len(key) != 8:
        print(Panel(
            Text('(×) ERROR: Length of plaintext or key is not 8', justify='center'),
            style='red bold',
        ))
        return

    des_encrypt(plaintext, key)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
