import math
from itertools import zip_longest, chain


"""
Given an array of length >= 0, and a positive integer N,
return the contents of the array divided into N equally sized arrays.
Where the size of the original array cannot be divided equally by N,
the final part should have length equal to the remainder.
"""


def get_chunk_size(size, target_chunks):
    """
    Get ideal chunk size given desired number of chunks and size of array
    :param size: size of array
    :param target_chunks: desired number of chunks
    :return:
    """
    return int(math.ceil(size/target_chunks))


def chunk_array(array, target_chunks):
    """
    Split an array into target number of equal sized chunks,
    the last chunk maybe shorter than the others if the size of array is
    not an exact multiple of target number of chunks
    :param array: array to chunk
    :param target_chunks: desired number of chuks
    :return: [[a b c] [d e f ]...] array of arrays
    """
    assert target_chunks > 0
    assert target_chunks <= len(array)
    if target_chunks == len(array):
        return [array]

    # go through array. fill buffer. when buffer hits desired size append
    # to result and flush buffer. this is naive implementation and works
    # but will not scale well beyond small arrays

    chunk_size = get_chunk_size(len(array), target_chunks)
    result = []
    buffer = []
    for ix in range(0, len(array)):
        if len(buffer) == chunk_size:
            result.append(buffer)
            buffer = []
        buffer.append(array[ix])
    if len(buffer) > 0:  # flush remainder
        result.append(buffer)
    return result


def iter_chunk_array(array, target_chunks):
    """
    As above, but uses itertools so should work with very large arrays
    :param array:
    :param target_chunks:
    :return:
    """

    def splitter(array, chunks):
        # splitter('ABCDEFG', 3) --> ABC DEF Gxx". Recipe from Python docs.
        args = [iter(array)] * chunks
        return zip_longest(*args, fillvalue=None)

    def non_null(array):
        return list(filter(lambda x: x is not None, iter(array)))

    chunk_size = get_chunk_size(len(array), target_chunks)
    return list(
            chain(
                non_null([item for item in bucket])
                for bucket in
                splitter(array, chunk_size)
            )
        )
