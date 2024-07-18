pangram = input("Give sentence. ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0
for i in pangram:
    if i in letters:
        answer += 1
        letters.remove(i)
if answer == 26:
    print("It is a pangram.")
else: print("It isn't a pangram.")