# list = [5, 6, 7, 8]
# new_list = [4, 3]
# list.extend(new_list)
# # print(list)

# list.append(20)
# # print(list)

# ##  SLICING  ##
# # print(list[-1:])


# ##  Searching in List  ##

# # if 20 in list:
# #     print(list.index(20))

# def searchInList(list, value):
#     for i in list:
#         if i == value:
#             return list.index(value)
#     return 'Element does not exist in the given list'

# print(searchInList(list, 20))

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'



print(fruit_list3)
