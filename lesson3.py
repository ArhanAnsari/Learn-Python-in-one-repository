#Lesson No.3:Printing in Colours
myName = input("Name: ")
myFavColor = input("Favourite Colour: ")

print(myName, "is your name")
print(myFavColor, "is your favourite colour")

"""
Colours Code
Colour | Code
_______________

Default | 0
Black | 30
Red | 31
Green | 32
Yellow | 33
Blue | 34
Purple |35
Cyan | 36
White | 37
"""

#Syntax
#print("\033[textcolorcode m your sentence to be printed(optional)")
#eg. print(\033[33mThis is Yellow Colour)
print("\033[36mThis is Cyan Color")
print("\033[0mThis is Default Color")
