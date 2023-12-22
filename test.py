from collections import defaultdict, deque


# my_dict1 =defaultdict(int)
# my_dict2 =defaultdict(str)
# my_dict3 =defaultdict(list)
# my_dict4 =defaultdict(set)
#
#
# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)
#
# print(my_dict1['myket'])
# print(my_dict2['myket'])
# print(my_dict3['myket'])
# print(my_dict4['myket'])
#
#
# my_dict1['my_key'] += 1
# print(my_dict1)
# print(my_dict1['my_key'])
#
# my_dict2['my_key'] += 'a'
# print(my_dict2)
# print(my_dict2['my_key'])
# #
# my_dict3['my_key'].append(3)
# print(my_dict3)
# print(my_dict3['my_key'])
# #
# # my_dict4['my_key'] += 1
# # print(my_dict1)
# # print(my_dict1['my_dict'])
#


Q = deque()
Q.append(4)
Q.append(5)
Q.append(6)
Q.append(7)
a = Q.popleft()
b = Q.pop()
print(Q, a, b)



