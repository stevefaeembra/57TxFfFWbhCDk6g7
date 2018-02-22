import unittest
from arraychunker import get_chunk_size


class TestArrayChunker(unittest.TestCase):

    def test_get_chunk_size(self):
        self.assertEqual(get_chunk_size(4, 4), 1)  # chunks one element each
        self.assertEqual(get_chunk_size(6, 2), 3)  # equal size chunks of 3
        self.assertEqual(get_chunk_size(5, 3), 2)  # expect 3 chunks of 2, [221]
        self.assertEqual(get_chunk_size(6, 1), 6)  # one chunk, whole array

    def test_split_even_size_chunks(self):
        self.assertEqual(True, False)

    def test_split_chunks_with_remainder(self):
        self.assertEqual(True, False)

    def test_split_into_no_chunks(self):
        self.assertEqual(True, False)

    def test_split_into_one_chunk(self):
        self.assertEqual(True, False)

    def test_spilt_into_too_many_chunks(self):
        self.assertEqual(True, False)

    def test_split_empty_array(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
