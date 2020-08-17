import unittest
from ._tools import *


class TestTools(unittest.TestCase):

    def test_num_to_bin_array(self):
        self.assertEqual(
            num_to_binlist(0),
            [0],
        )
        self.assertEqual(
            num_to_binlist(1),
            [1],
        )
        self.assertEqual(
            num_to_binlist(5, length=4),
            [0, 1, 0, 1],
        )
        self.assertEqual(
            num_to_binlist(10, length=3),
            [1, 0, 1, 0],
        )
        self.assertEqual(
            num_to_binlist(0b110101100),
            [1, 1, 0, 1, 0, 1, 1, 0, 0],
        )
        self.assertEqual(
            num_to_binlist(0b110101101),
            [1, 1, 0, 1, 0, 1, 1, 0, 1],
        )

    def test_to_bin_array(self):
        self.assertEqual(
            bytes_to_binlist(b'Fuck You'),
            [
                0, 1, 0, 0, 0, 1, 1, 0,
                0, 1, 1, 1, 0, 1, 0, 1,
                0, 1, 1, 0, 0, 0, 1, 1,
                0, 1, 1, 0, 1, 0, 1, 1,
                0, 0, 1, 0, 0, 0, 0, 0,
                0, 1, 0, 1, 1, 0, 0, 1,
                0, 1, 1, 0, 1, 1, 1, 1,
                0, 1, 1, 1, 0, 1, 0, 1,
            ],
        )

    def test_lshift(self):
        l = [0, 1, 2, 3, 4]
        lshift(l, 3)
        self.assertEqual(l, [3, 4, 0, 1, 2])

        l = [0, 1, 2, 3, 4]
        lshift(l, 8)
        self.assertEqual(l, [3, 4, 0, 1, 2])

    def test_permute_with(self):
        l = [3, 9, 8, 2, 7]
        pc = [4, 0, 1, 0, 2, 4, 3]

        self.assertEqual(
            permute_with(l, table=pc),
            [7, 3, 9, 3, 8, 7, 2],
        )

    def test_binlist_xor(self):
        a = [0, 1, 0, 0, 1]
        b = [1, 0, 1, 0, 0]

        self.assertEqual(
            binlist_xor(a, b),
            [1, 1, 1, 0, 1],
        )

    def test_split_every(self):
        self.assertEqual(
            split_every([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        )

    def test_split_half(self):
        self.assertEqual(
            split_half([1, 2, 3, 4, 5, 6]),
            [[1, 2, 3], [4, 5, 6]],
        )

    def test_bin_array_to_num(self):
        self.assertEqual(
            binlist_to_num([1, 1, 0, 0, 1, 0, 1]),
            0b1100101,
        )
