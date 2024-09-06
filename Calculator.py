def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a/b)
def mul(a,b):
    print(a*b)
while True:
        try:
            a=int(input("Enter The First Digit :"))
            b=int(input("Enter The Second Digit :"))
            symbol=str(input("""press number
                1.addtion
                2.subtraction
                3.divide
                4.multiplication
                    """))
            if symbol=="1":
                add(a,b)
            elif symbol=="2":
                sub(a,b)
            elif symbol=="3":
                div(a,b)
            elif symbol=="4":
                mul(a,b)
            a=str(input("Do you want another calculation y/n "))
            if a=="N":
                break
        except Exception as e:
            print("invalid input")




     