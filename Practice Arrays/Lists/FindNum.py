import numpy as np

MyArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

def FindNum(array, target):
    for i in range(len(array)):
        if array[i] == target:
            print(i)
FindNum(MyArray, 4)