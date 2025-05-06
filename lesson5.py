#Lesson No. 5: If-elif-else statements
# Multiple if -> elif

# myName = input("Name: ")

# if myName == "Arhan":
#     print("Hello, Arhan!")

# elif myName == "Ahmad":
#     print("Hello, Ahmad!")

# else:
#     print("Hello, Unknown!")

# name = input("name:")

# if name == "Arhan":
#     print("Hello, Arhan!")

# elif name == "Ahmad":
#     print("Hello, Ahmad!")

# Secure Login System using Python
print(" SECURE LOGIN ")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "arhan" and password == "4523":
    print("Welcome Arhan!")

elif username == "ahmad" and password == "4525":
    print("Welcome Ahmad!")

else:
    print("Go away!")

# and -> Logical AND 
# requires both conditions to be true
# 0 -> False
# 1 -> True
# True -> 1 & 1
# False -> 0 & 0
# False -> 0 & 1
# False -> 1 & 0