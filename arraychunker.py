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
    return size//target_chunks
