import random

words = ["dog","red","pyautogui","the flash","fortnight"]

hint1 = ["not a cat","color wheel","Mr. Rosenfeld","Barry Allen","All day, everyday"]

hint2 = ["fluffy","oposite of orange","computers","cisco ramon","tactical shotgun"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 1

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'firstletter', 'last letter', or 'give up' for help")
    guess = input()

    if guess == secretword:
        print("You Win! It took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])
    elif guess == "hint2":
        print(hint2[number])
    elif guess == "first letter":
        print(secretword[0])
    elif guess == "last letter":
        print(secretword[-1])
    elif guess == "give up":
        print("The word was " + secretword)
        break
    else:
        counter += 1
