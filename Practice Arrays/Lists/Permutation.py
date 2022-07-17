def Permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

list1 = [1,2,4]
list2 = [2,1,6]

print(Permutation(list1, list2))