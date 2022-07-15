MyList = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
temp = []
def UniqueList(list):
    for i in list:
        if i in temp:
            print(i)
            return False
        else:
            temp.append(i)
    return True
print(UniqueList(MyList))
