import math

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
    return []
