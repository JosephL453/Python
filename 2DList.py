list1 = [5,8,3,7,2,1,4,5,7,6]
# print(list1)
# for i in list1:
#     print(i)
# list1.append(6)
# print(list1)
# for i in list1:
#     print(list1.index(i), i)
# for i in range(len(list1)):
#     print(i, list1[i])
# rl = list(reversed(list1))
# print(rl)
# del list1[8]
# print(list1)
# list1.remove(8)
# print(list1)
# print(list1.pop(5))
# print(list1)
# n = len(list1)
# print(list1[5:n:2])
# print(list1[::-1])

list2 = [[1,2,3,],[4,5,6],[7,8,9]]
# print(list2)
# print(len(list2))
# print(list2[1][1])
# print(len(list2[0]))
# for i in range(0, len(list2)):
#     for j in range(0, len(list2[i])):
#         print(list2[i][j], end = " ")
#     print("\n")
list3 = [[9,8,7],[6,5,4],[3,2,1]]
list4 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        list4[i][j] = list3[i][j] * list2[i][j]
print(list4)
