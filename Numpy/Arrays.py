import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    revarr = numpy.flip(arr)
    return revarr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
