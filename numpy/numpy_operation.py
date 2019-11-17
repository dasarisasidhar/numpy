import numpy as np

def d_types():
    t1 = np.float32(1.0)
    t2 = np.int_([1,2,4])
    t3 = np.arange(3, dtype=np.uint8)
    t4 = np.array([1, 2, 3], dtype='f')  #convert to float type
    t5 = np.array([1,2,3])
    t6 = t5.astype(float)  #convert to float type
    t7 = np.int8(t5)  # convert to float type 
    t8 = t6.dtype  #type of data
    t9 = np.issubdtype(t6, np.integer) #gives bool
    np.power(100, 8, dtype=np.int64) #np.power(100, 8, dtype=np.int32) gives over flow so use 64
    np.iinfo(int32) #give the range and other info.

def hacker_earth_1():
    arr = input().strip().split(' ')
    result = np.array(arr)
    data = np.array(arr,int)
    reshaped = data.reshape(3,3)
    print(reshaped)

def hacker_earth_2():
    float_data = numpy.array(arr,float)
    data = numpy.flipud(float_data)
    return data

arr = input().strip().split(' ')
result = hacker_earth_2(arr)
print(result)




d_types()