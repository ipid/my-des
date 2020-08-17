__all__ = (
    'binlist_to_str',
    'num_to_binlist',
    'bytes_to_binlist',
    'lshift',
    'permute_with',
    'binlist_xor',
    'split_every',
    'split_half',
    'binlist_to_num',
)

from typing import List
import math


def binlist_to_str(x: List[int], every: int = 8) -> str:
    res = []
    for i, elem in enumerate(x):
        res.append(str(elem))
        if i % every == every - 1:
            res.append(' ')

    return ''.join(res).rstrip()


def num_to_binlist(x: int, *, length=...) -> List[int]:
    if x < 0:
        raise ValueError('x 不能小于 0')
    if x == 0:
        if isinstance(length, int):
            return [0] * length
        else:
            return [0]

    res = []
    while x != 0:
        bit = x & 1
        x >>= 1

        res.append(bit)

    res.reverse()
    if isinstance(length, int) and len(res) < length:
        res = [0] * (length - len(res)) + res

    return res


def bytes_to_binlist(x: bytes) -> List[int]:
    result = []

    for b in x:
        for i in range(7, -1, -1):
            bit = b & (1 << i)
            if bit > 0:
                bit = 1

            result.append(bit)

    return result


def lshift(x: List[int], num: int) -> None:
    if num < 0:
        raise ValueError('num 不能为负数')
    if num >= len(x):
        num %= len(x)

    for i in range(num):
        x.append(x.pop(0))


def permute_with(x: List[int], *, table: List[int]) -> List[int]:
    return [x[i] for i in table]


def binlist_xor(a: List[int], b: List[int]) -> List[int]:
    if len(a) != len(b):
        raise ValueError('a 与 b 的长度不同')

    return [m ^ n for m, n in zip(a, b)]


def split_every(x: List[int], length: int) -> List[List[int]]:
    if len(x) % length != 0:
        raise ValueError('x 不能被等长分割为 length 份')

    result = []
    for i in range(len(x) // length):
        result.append(x[i * length: (i + 1) * length])

    return result


def split_half(x: List[int]) -> List[List[int]]:
    if len(x) % 2 != 0:
        raise ValueError('x 无法对半分')

    half_len = len(x) // 2
    return [x[:half_len], x[half_len:]]


def binlist_to_num(x: List[int]) -> int:
    res = 0
    for i, elem in enumerate(reversed(x)):
        res += elem * (1 << i)
    return res
