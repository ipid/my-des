__all__ = (
    'des_encrypt',
    'des_decrypt',
)

from typing import List, Any
from ._tools import *
from ._constant import *
from rich import print
from rich.text import Text
from rich.panel import Panel


def keygen(key: bytes) -> List[List[int]]:
    res = []

    key = bytes_to_binlist(key)
    key = permute_with(key, table=PC_1)
    print(f'[red b]Key after PC-1[/]: {binlist_to_str(key, 7)}\n')
    c, d = split_half(key)

    for i in range(16):
        print(f'[white b u]Round {i}[/]')
        lshift(c, ROTATION[i])
        lshift(d, ROTATION[i])
        print(f'[red b]Rotated key[/]: {binlist_to_str(c, 7)} | {binlist_to_str(d, 7)}')
        key = permute_with(c + d, table=PC_2)
        print(f'[red b]Key after PC-2[/]: {binlist_to_str(key, 6)}')
        res.append(key)
        print('')

    return res


def f_func(x: List[int], *, key: List[int]) -> List[int]:
    x = permute_with(x, table=E)
    print(f'[red b]r[/] (Permutated): {binlist_to_str(x)}')
    x = binlist_xor(x, key)
    print(f'[red b]r xor key[/]: {binlist_to_str(x)}')

    res = []
    for i, binlist in enumerate(split_every(x, 6)):
        num = binlist_to_num(binlist)
        res += num_to_binlist(S[i][num], length=4)

    return permute_with(res, table=P)


def des_encrypt_core(x: List[int], keys: List[List[int]]) -> List[int]:
    print('')
    print(Panel(Text('Stage 2. Initial Permutation', 'green bold', justify='center')))
    print(f'Plaintext = {binlist_to_str(x)}')
    x = permute_with(x, table=IP)
    print(Text('↓ After IP: ↓', justify='center'))
    print(f'Plaintext = {binlist_to_str(x)}\n')
    l, r = split_half(x)

    print(Panel(Text('Stage 3. Feistel structure', 'green bold', justify='center')))
    for i in range(16):
        print(f'[white b u]Round {i}[/]')
        print(f'[red b]l[/] = {binlist_to_str(l)}')
        print(f'[red b]r[/] = {binlist_to_str(r)}')

        r_new = binlist_xor(l, f_func(r, key=keys[i]))
        l_new = r

        l, r = l_new, r_new

        print(f'[red b]Encrypted:[/] {binlist_to_str(l)} {binlist_to_str(r)}\n')

    print(Panel(Text('Stage 4. Swap and Reverse IP', 'green bold', justify='center')))
    l, r = r, l
    print(f'[red b]Swaped ciphertext[/]: {binlist_to_str(l)} {binlist_to_str(r)}')
    after_fp = permute_with(l + r, table=FP)
    print(f'[red b]After FP[/]: {binlist_to_str(after_fp)}\n')

    return after_fp


def des_encrypt(x: bytes, key: bytes) -> List[int]:
    x = bytes_to_binlist(x)

    print(f'[red b]Plaintext:[/] {binlist_to_str(x)}')
    print(f'[red b]Key:[/] {binlist_to_str(bytes_to_binlist(key))}\n')
    print('')
    print(Panel(Text('Stage 1. Generate keys', 'green bold', justify='center')))

    keys = keygen(key)
    ciphertext = des_encrypt_core(x, keys)

    print('[white]Finally we got our ciphertext:[/]')
    print(binlist_to_str(ciphertext))

    return ciphertext


def des_decrypt(x: bytes, key: bytes) -> List[int]:
    x, keys = bytes_to_binlist(x), keygen(key)
    keys = [*reversed(keys)]
    return des_encrypt_core(x, keys)
