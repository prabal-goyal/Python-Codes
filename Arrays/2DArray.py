import numpy as np

Array2D = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(Array2D)


##  INSERTION  ##

##  new name = np.insert(previous array, index, data, axis=0 for column--1 for row)

newArray2D = np.insert(Array2D, 0, [10,11,12], axis = 0)
print(newArray2D)

##  Accessing an Element  ##

def accessElement(array, rowindex, colindex):
    if rowindex >= len(array) or colindex >= len(array[0]):
        print("Wrong Index")
    else:
        print(array[rowindex][colindex])

#accessElement(newArray2D,3,2)

##  Traverse a 2D array  ##

def traverse2Darray (array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

#traverse2Darray(newArray2D)


##  Searching an Element  ##

def search2DArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at ' + str(i) + ' ' + str(j) + '.'
    return 'Value not found.'

print(search2DArray(newArray2D,20))