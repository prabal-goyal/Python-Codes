MyList = [84,85,86,85,97,90]
a = MyList
a.sort(reverse=True)

print(a)

first = a[0]

second = None

for i in MyList:
    if i != first:
        i = second
    print(first, second)