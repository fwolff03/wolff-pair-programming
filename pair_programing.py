#call import for numpy
import numpy as np
def offset_mean(array, value):
    """offset the mean of the given array by the wanted mean value
    Take the given input array and return the array with an offset that alters the mean to the wanted mean value
    Parameters
    __________
    array : ndarray
    value : int or float
    Returns
    __________
    offset : ndarray
    """
    assert(type(array) == np.ndarray)
    assert(type(value) == float) or (type(value) == int)
    #find the original mean
    current_array_mean = array.mean()
    #find the offset by taking the wanted mean value minus the current
    offset = value - current_array_mean
    #find the wanted offset from array plus the found offset
    offset_array = array + offset
    return offset_array