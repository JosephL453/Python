password = {
    'Password1': 1,
    'Password2': 12,
    'Password3': 123,
    'Password4': 1234,
    'Password5': 12345,
    'Password6': 123456,
    'Password7': 1234567,
    'Password8': 12345678,
    'Password9': 123456789,
    'Password10': 12345678910
}
u = input("What is the username? ")
if u in password:
    p = int(input("What is the password? "))
    if password[u] == p:
        print("You have logged into the system.")
    else:
        print("Incorrect Password")
else:
    print("Username not in system.")
