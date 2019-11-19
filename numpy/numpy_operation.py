import numpy as np
from io import StringIO

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
    arr = input().strip().split(' ')
    float_data = numpy.array(arr,float)
    data = numpy.flipud(float_data)
    return data

def Array_creation():
    """
    Conversion from other Python structures (e.g., lists, tuples)

    Intrinsic numpy array creation objects (e.g., arange, ones, zeros, etc.)

    Reading arrays from disk, either from standard or custom formats

    Creating arrays from raw bytes through the use of strings or buffers

    Use of special library functions (e.g., random)
    """
    arr1 = np.array([2,3,1,0])  #from list
    arr2 = np.array([[1,2.0],[0,0],(1+1j,3.)]) #from list and tuple
    arr3 = np.zeros((2, 3)) #from zeros
    arr3 = np.ones((2, 3)) #from ones
    arr4 = np.arange(2, 10, 2, dtype=float) #from 2 till 10 having 2 step size of type float
    arr5 = np.linspace(1., 4., 6) # from 1 including 4 split 6 equal parts
    arr6 = np.indices((3,3))
    arr7 = np.indices((4,4))
    arr8 = np.indices((2,3))
    arr9 = np.indices((3,2))
    print(arr6, arr7, arr8, arr9)
    #indices() will create a set of arrays (stacked as a one-higher dimensioned array), one per dimension with each representing variation in that dimension


def IO_with_numpy():
    """
    "from io import StringIO" to get text input
    "genfromtxt" - to process
            Load data from a text file, with missing values handled as specified.
            Each line past the first skip_header lines is split at the delimiter character, 
            and characters following the comments character are discarded.
            note:
                In a nutshell, genfromtxt runs two main loops. The first loop converts each line of the file in a sequence of strings.
                The second loop converts each string to the appropriate data type. This mechanism is slower than a single loop, but gives more flexibility.
                In particular, genfromtxt is able to take missing data into account, when other faster and simpler functions like loadtxt cannot.
    """
    data = u"1, 2, 3\n4, 5, 6" #data with newline to read that use the following
    value1 = np.genfromtxt(StringIO(data), delimiter=",") #gives 2d matrix of values  
    data = u"  1  2  3\n  4  5 67\n890123  4"
    value2 = np.genfromtxt(StringIO(data), delimiter=3) #it will take delimiter 3 so takes 3 positions for each values including spaces and not including /n
    data = u"123456789\n   4  7 9\n   4567 9"
    value3 = np.genfromtxt(StringIO(data), delimiter=(4, 3, 2)) #first row contains 4 and second 3 and 3rd 2 positions respectively
    data = u"1, abc , 2\n 3, xxx, 4"
    value4 = np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True) # auto strip will remove white spaces 
    data4 = data = u"""# for comments and large data
                    # Skip me !
                    # Skip me too !
                    1, 2
                    3, 4
                    5, 6 #This is the third line of the data
                    7, 8
                    # And here comes the last line
                    9, 0
                    """
    values5 = np.genfromtxt(StringIO(data), comments="#", delimiter=",") #All the data inside # will be removed
    data = u"\n".join(str(i) for i in range(10))
    value6 = np.genfromtxt(StringIO(data), skip_header=3, skip_footer=5) #removes 3 values from first and 5 from last
    np.genfromtxt(StringIO(data), usecols=(0, -1)) # only cols 0 and last will be selected
