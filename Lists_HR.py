name = "Halsey Robinson"
games = ["Fortnite","GTA","Assassins Creed","Battlefront"]

print("My name is " + name)

#print(games)

for i in games:
    print("One of my games is " + i)



actors = ["Matt Damon","Danny Divido","The Rock"]

for i in actors:
    if i == "Matt Damon":
        print(i + " is in a lot of movies")
    elif i == "Danny Divido":
        print(i + " is short and bald")
    elif i == "The Rock":
        print(i + " is really strong")



teams = []

while True:
    print("Who are your favorite teams? Type 'end' to quit")
    answer = input()
    if answer == "end":
        break
    else:
        teams.append(answer)

for i in teams:
    print("One of your favorite teams is " + i)
if teams == "Giants" or "Patriots" or "Jets":
    print("The " + i + " suck")
elif teams == "Eagles":
    print("Tru")
else:
    print("Wrong Answer")

