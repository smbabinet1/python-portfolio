#Scarlett 
#11/20
#Pokemon Evolution Game
#Init
pokemon_level = 0
pokemon_name = "babysnorlax"
day = 1
import random
#Functions
def evolve():
    global pokemon_level
    global pokemon_name
    if pokemon_level == 5:
        pokemon_name == "teensnorlax"
        print("Your Pokemon Has Evolved to teensnorlax!")
        draw_teensnorlax()
    elif pokemon_level == 10:
        pokemon_name == "adultsnorlax"
        print("Your Pokemon Has Evolved to adultsnorlax!")
        draw_adultsnorlax()
def draw_babysnorlax():
    print("""Ƶƶ(￣▵—▵￣)""")
def draw_teensnorlax():
    print("""⠀⠀⠀⠀⠀⠀⠀⢠⣤⣀⠀⠀⠀⠀⢀⣀⣤⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⢀⠀⠀⠀⢸⡿⠛⠛⠛⠛⠛⠉⠛⢿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣿⣿⣿⣄⠀⣼⠀⠀⠀⢂⣀⣀⡀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⡷⠋⠈⠀⠀⠀⠀⠀⠀⠀⠈⠘⠣⡀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣦⡀⠀⠀
⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣦⠀
⠀⠀⣸⣿⣿⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⠀⣤⡟⠛⠋⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠈⠋⠈⢿⣿⡿
⢀⡉⠀⠀⣀⣤⣄⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣤⣤⣄⠀⠀⣴⡄
⠘⢇⠀⠰⣿⣿⢟⢼⣿⣿⣿⣿⣿⣿⣿⣿⡿⢜⠿⠿⠿⠀⡀⠀⠀
⠀⠀⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠈⠀⠀⠀""")
def draw_adultsnorlax():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣬⣿⡿⠿⢿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠁⠀⠉⠙⠻⠿⣶⣦⣀⣠⣤⣤⣤⣤⣤⣤⣶⠿⠟⠫⠉⠀⠀⢀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣀⣠⣤⠤⣤⣤⣀⡒⠀⣀⣤⡤⠶⠶⠤⣄⡀⠤⣀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣠⡼⠛⠉⠀⠀⠀⠀⠀⠈⠙⠟⠉⠀⠀⠀⠀⠀⠈⠙⠳⣏⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣤⣿⣻⣿⣿⣷⣿⣧⠀⠀⠀⠀⠀⢸⣿⣸⠋⠀⠠⠴⠶⠒⠒⠲⠆⠀⠀⠀⠀⠘⠓⠒⠒⠲⠶⠀⠀⠈⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢴⡿⣿⡿⠋⠉⠩⠙⣿⣿⣄⠀⠀⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠀⣠⣿⣄⣀⣀⣀⣀⣀⣴⣄⠀⠀⠀⠀⠀⠀⡇⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⡿⠁⠀⠀⠀⠀⠹⣿⣿⣷⣄⠀⢰⣿⣿⠀⠀⠀⠀⠀⢀⣀⣨⣤⣤⠤⠤⠤⠤⠤⣬⣭⣄⣀⣀⠀⢀⡼⠁⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣼⣿⣿⣠⠴⠖⠚⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⠶⢤⣸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⢰⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡼⡀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⢿⣻⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣧⢅⠀⠀⢀⡾⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠘⡇⠹⣇⠙⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⡌⡀⣰⡟⢡⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⡗⠀⠹⣆⠀⠙⢿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣧⣰⡟⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⣰⠿⠀⠀⢻⡄⠀⠀⠙⢿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⡟⡄⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠃⠀⠀⢀⣴⠏⠂⠀⠀⠘⣧⡀⠀⠀⠀⠻⣷⡀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⢹⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⣀⣠⣤⡴⠶⠒⠒⠛⠛⠛⠛⠛⠛⢛⠛⠒⠒⠒⠒⠶⠶⠶⠶⠿⠥⠤⠤⠴⠶⡟⠁⠀⠀⠀⢀⠀⣿⠀⠀⠀⠀⠀⠹⣷⡀⠀
⠀⠀⠀⠀⠀⣼⡏⠀⢠⣄⠀⠀⠀⠀⠉⠙⠛⠉⠉⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢀⣠⠾⢻⡇⢻⢀⠀⠀⠀⠀⠀⢻⣇⠀
⠀⠀⠀⠀⠀⣿⡇⠀⣾⠉⠷⣄⣂⣂⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢴⡟⠁⠀⣼⣧⣼⡧⠄⢀⣠⣤⠀⣿⣿⣦
⠀⢀⣄⣀⣀⣿⣧⡶⢿⣀⣠⡼⠋⠉⠉⠙⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠉⠀⠈⠷⣤⠾⠛⠀⢨⡽⠟⠋⣩⣯⣾⣿⣙⣿
⠀⠸⣿⡉⠉⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣠⣶⣿⢿⣿⣯⣿⡏
⠀⠀⢹⣷⣀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠹⣿⣿⣿⠛⠁
⠀⢠⣿⠁⠀⠀⠀⠀⠀⢀⡴⠚⠉⢉⣉⣉⠉⠉⠒⠲⣿⣿⣿⣎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⡠⣖⣦⣭⣤⣥⣐⠒⠦⢄⡀⠀⠀⠀⡤⠿⣿⣦⣤⠀
⣤⣾⣇⣀⡀⠀⠀⠀⣠⠎⣠⡴⠛⠉⠉⠉⠹⣆⠀⢀⣿⣿⣿⣿⡄⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⣿⢀⠎⣾⠋⠀⠀⠀⠀⠉⠳⣄⠀⠙⡄⠀⠀⣧⣀⣤⡾⠟⠀
⢿⣥⣀⣺⠇⠀⠀⢠⠇⣰⠏⠀⠀⠀⠀⠀⠀⣿⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡜⠀⣇⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠁⠀⠀⢸⣿⠁⠀⠀⠀
⠀⠹⣿⡁⠀⠀⠀⢸⠀⣯⠀⠀⠀⠀⠀⢀⣴⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⢦⡀⠀⠀⠀⣀⣴⠏⠀⢀⡇⠀⣰⡿⠁⠀⠀⠀⠀
⠀⠀⠈⢿⣦⡀⠀⠀⢣⡘⢦⣄⣀⣤⠶⠋⣡⣾⠟⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠟⢿⣦⣀⠉⠉⠉⠉⠉⠀⢀⡤⢋⣠⡾⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⡛⣷⣶⣤⡭⠷⠤⣤⣴⣶⣟⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣻⣿⣷⣶⣶⣶⣴⣷⣾⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀""")
def train():
    global day
    global pokemon_level
    day = day + 1
    pokemon_level = pokemon_level + 1
    print("You Leveled Up! Your Pokemon is Now Level " + str(pokemon_level) + "!")
    evolve()
def battle():
    global pokemon_level
    global day
    day = day + 1
    outcome = random.randint(1,2)
    if outcome == 1:
        pokemon_level = pokemon_level + 2
        print("You won the battle! +2")
        print("Your Pokemon is Now Level " + str(pokemon_level) + "!")
    else:
        print("You Lost the Battle! +0")
        print("Your Pokemon is Still Level " + str(pokemon_level) + "!")
    evolve()
def rest():
    global pokemon_level
    global pokemon_name
    global day
    day = day + 1
    print("Your Pokemon is Level " + str(pokemon_level) + "!")
    if pokemon_level >= 10:
        pokemon_name = "adultsnorlax"
        print(str(pokemon_name))
        draw_adultsnorlax()
    if pokemon_level >= 5:
        pokemon_name = "teensnorlax"
        print(str(pokemon_name))
        draw_teensnorlax()
    else:
        pokemon_name = "babysnorlax"
        print(str(pokemon_name))
        draw_babysnorlax()


def PokeEvoSim():
    global day
    global pokemon_level
    print("Welcome to Pokemon Evolution Simulator!")
    while True:
        print("Choose an activity. Day: " + str(day))
        print("""1. Train
2. Gym Battle
3. Rest (Display Info)
4. Exit""")
        option = int(input("(1-4) Option: "))
        if option == 1:
            train()

        elif option == 2:
            battle()

        elif option == 3:
            rest()
        elif option == 4:
            break

#Main
PokeEvoSim()



