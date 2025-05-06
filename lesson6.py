# Lesson No. 6: Nesting
# Variable Declareation
tvShow = input("What is your favorite TV show? ")

if tvShow == "Peppa Pig":
    print("ugh, why?")
    favCharacter = input("Favorite Character: ")
    if favCharacter == "Daddy Pig":
        print("Right answer!")

    else:
        print("Nah! Daddy Pig's Greatest")

elif tvShow == "Paw Patrol":
    print("Aww, sad times!")

else:
    print("Yeah, that's cool and all!")
