import numpy as np

Mylist = [1,2,4,5,6,7,8,9,10]

def MissingNumber(array, totalcount):
    expectedSum = totalcount*(totalcount+1)/2
    sum = 0
    for i in array:
        sum += i
    return int(expectedSum-sum)
    
    
print(MissingNumber(Mylist, 10))

# Mylist = [1,2,4,5,6,7,8,9,10]
# sum=0
# for i in Mylist:
#     sum += i
# print(sum)