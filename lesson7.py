# Lesson No.7: Casting\
# Casting -> Conversion of one type to another
# String -> Integer
# Types of Data Types:
# str - string
# int - integer
# float - decimal no.
# bool - boolean (True/False) 


# Will throw an error of type error
# myScore = input("Enter your score: ")
# if myScore > 100000:
#     print("Winner!")

# else:
#     print("Try again!")

# Corrected code
myScore = int(input("Enter your score: ")) # Coverting string to integer
if myScore > 100000:
    print("Winner!")

else:
    print("Try again!")

# Types of Comparison Operators:
# > - greater than
# < - Less than
# >= - greater than or equal to
# <= - less than or equal to
# == - equal to
# != - not equal to

points = 1520
print(type(points)) #type() function returns the type of the variable
print(points)

print("Points: " + str(points)) # converting integer to string

bool = True
print(type(bool))
print(bool)

bool = False
print(type(bool))
print(bool)

float = 4.56
print(type(float))
print(float)

str = "Hello"
print(type(str))
print(str)

str = 'Hello'
print(type(str))
print(str)

myMoney = int(input("Enter the amount of money: "))
if myMoney >= 45250000000000:
    print("you are the richest")

else:
    print("you are the poorest")