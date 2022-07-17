List = [1,1,2,2,3,4,5]
newList=[]
def removeduplicates(list):
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList
print(removeduplicates(List))
