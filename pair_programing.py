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
    # You might want to add descriptions for your parameters and your return value. -Grey
    # Everything else looks good -Grey
    # I like your comments throughout the code -Grey
    
    assert(type(array) == np.ndarray) #I think you need to add a message error for the assert functions, otherwise they don't work. You could add something like "parameter must be an array" -Grey
    assert(type(value) == float) or (type(value) == int)
    #find the original mean
    current_array_mean = array.mean()
    #find the offset by taking the wanted mean value minus the current
    offset = value - current_array_mean
    #find the wanted offset from array plus the found offset
    offset_array = array + offset
    return offset_array

def testFunction():
    assert(all(offset_mean(np.array([1,3,5,7,9]),9.0) == np.array([5., 7., 9., 11., 13.]))), "Test 1 Failed"
    assert(all(offset_mean(np.array([-3, -5, -7]),4) == np.array([6, 4, 2]))), "Test 2 Failed"
    print("All tests passed")
testFunction()