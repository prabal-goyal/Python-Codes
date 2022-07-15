from array import *

arr1 = array('i', [1,2,3,4,5,6,7])

def AccessAnElement(array, index):
    if index >= len(array): 
        print("No element at this location.")
    else:
        print(array[index])

AccessAnElement(arr1, 7)

## Time Complexity is O(1)  ##



def SearchAnElement(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element does not exist."

print(SearchAnElement(arr1, 5))

