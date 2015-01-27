import math
def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    try:
        return math.pow(array[n], n)

    except IndexError:
        return -1



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000
    assert index_power([0, 1], 0) == 1
    assert index_power([1, 2], 3) == -1
