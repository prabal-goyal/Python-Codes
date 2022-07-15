##        Array can store data of specified type                      ##
##        Elements of an array are located in contiguous              ##
##        Each element of an array has unique index                   ##
##        The size of an array is predefined and cannot be modified   ##



##     from array import * ##
##     variable = array('typecode(type of array)', [values])  ##

from array import *

arr1 = array('i', [1,2,4,7,6])

#print(arr1)

##  arr1.insert(index, value)  ##

arr1.insert(0,9) #------------> Time Complexity = O(n) [also when value is added between it remains same] {time consuming task as values are being shifted to right}
print(arr1)

arr1.insert(7,8) #------------> Time Complexity = O(1) {no task done only value added at last}
print(arr1)


##    Traverse a Array (Time Complexity is O(n))   ##

def TraverseArray(array):
    for i in array: #-------> O(n)
        print(i)    #-------> O(1)

TraverseArray(arr1)




##  Deleting an Element  ##
##  array.remove(element)  ##

arr1.remove(2)

print(arr1)