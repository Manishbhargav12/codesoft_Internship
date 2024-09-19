import random
passLength=int(input("Enter Your Password Length "))
def password(Length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_string = ""
    for i in range(Length):
        random_string += random.choice(characters)
    return random_string
print(password(passLength))
print("Your Password Is Ready Copy To Use This")