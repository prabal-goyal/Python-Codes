MyList = [1,2,3,4,5,1,3,2,1,3,3,7,2,5]

def TwoSum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                print(i, j)
TwoSum(MyList, 3)

print(len(MyList))