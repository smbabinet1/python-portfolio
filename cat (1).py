#Scarlett
#Init
#Functions
#Run Cat Game
def PlayCatGame():
    print ("Which Animated Cat Are You?")
    print ("Answer the Questions to Find Out")
    ans = input("Do you prefer savory (sa) or sweet (sw)?")
    if ans == "sa":
        ans = input("Do you prefer oranges (o) or apples (a)?")
        if ans == "o":
            ans = input("Would you consider yourself lazy (l) or adventurous (a)?")
            if ans == "l":
                print("Your Cartoon Cat is Garfield!")
            else:
                print("Your Cartoon Cat is Hobbes!")
        if ans == "a":
            ans = input("Do you prefer wearing shoes (s) or being barefoot (b)?")
            if ans == "s":
                print("Your Cartoon Cat is Pete the Cat!")
            else:
                print("Your Cartoon Cat is Tom")
    if ans == "sw":
        ans = input("Do you prefer blue (bl) or pink (pi)?")
        if ans == "bl":
            ans = input("Would you consider yourself clumsy (c) or sneaky (sn)?")
            if ans == "c":
                print("Your Cartoon Cat is Gumball!")
            else:
                print("Your Cartoon Cat is Pink Panther!")
        if ans == "pi":
            ans = input("Would you consider yourself mischevious (m) or good (g)?")
            if ans == "m":
                print("Your Cartoon Cat is Cheshire Cat!")
            else:
                print("Your Cartoon Cat is Hello Kitty!")


#Main
PlayCatGame()
