mylist = [1,2,4,5,3,7,-2,11]

# def TwoSum(list, target):
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] + list[j] == target:
#                 print(i, j)
# TwoSum(MyList, 3)


def pairsum(list,sum):
    newlist = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == sum:
                newlist.append(str(mylist[i])+"+"+str(mylist[j]))
    return newlist

print(pairsum(mylist,9))