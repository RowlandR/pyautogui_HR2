print("What is your favorite sport?")

sport = input().title()
if sport == "tennis":
    print("Mine too!")
elif sport == "baseball":
    print("Great Sport")
else:
    print("Nice!")

print("What is your favorite number?")

number = input().title()
if number == "13":
    print("Lucky Number 13")
elif number == "7":
    print("Mine too!")
else:
    print("Nice!")

print("What is your favorite show?")

show = input().title()
if show == "the flash":
    print("Mine too!")
elif show == "The Office":
    print("Who is your favorite character?")
    theoffice = input().title()
    if theoffice == "Jim":
        print("Agreed")
    elif theoffice == "dwight":
        print("FACT! Bears eat beats. Bears, beats, battlestar galactica")
    else:
        print("Sweet")
else:
    print("Nice!")

print("What is your favorite video game?")

videogame = input().title()
if videogame == "mario":
    print("Nice chioce!")
elif videogame == "minecraft":
    print("Woooooooow")
elif videogame == "assassins creed":
    print("Good chioce")
else:
    print("Nice!")

print("What is your favorite book?")
book = input().title()
if "harry potter" in book:
    print("Good chioce!")
elif "percy jackson" in book or "magnus chase" in book or "the kane chronicles" in book or "the apollo trials" in book:
    print("Rick Riordon is the best writer.")
elif "the young elites" in book:
    print("Who is your favorite character?")
    elites = input().title()
    if elites == "Enzo" or "violeta":
        print("creepy")
    else:
        print("Cool!")
