# textbooks = {
#             'Math': 60,
#             'Science': 70,
#             'Physics': 150,
#             'History': 120
#             }
# textbooks['Physics'] = 200
# textbooks['Biology'] = 130
# textbooks['English'] = 175
# i = input("Which Book Do You Want To See? ")
# if i in textbooks:
#     print(i, textbooks[i])
# else:
#     print("Book Not In Stock.")
# for k,j in textbooks.items():
#     print(k,j)

# Nested Dictionary:

# names = {
#     'Joseph': {
#         'age': 14,
#         'marks': [100, 98, 99, 97, 100]
#     },
#     'Bob': {
#         'age': 15,
#         'marks': [99, 100, 96, 97, 97]
#     }
# }
# print(names['Joseph']['age'])
count = 0
word = input("Give A Word.")
vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}
for i in word:
    if (i in vowels):
        vowels[i] += 1
print(vowels)

