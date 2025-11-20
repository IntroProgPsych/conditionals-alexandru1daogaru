age = int(input("Type your age"))
if age>=18 and age<100:
    print("You are an adult")
elif age>=100:
    print("You are too old boy")
elif age<0:
    print("you are not born yet")
else:
    print("You are a child")