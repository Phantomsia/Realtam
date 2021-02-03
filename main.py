name = input("What is your name?: ")#name system
print("Welcome " + name)
print("to Realtam! Realtam takes place in year 1040. The Earth is covered in snow and you live in the woods! The only things near")
print("are Outpost that are miles away! You get very hungry and need some food! Go on the quest to get some good food!")

crossroad1 = input("""
You wake up after sleeping, where will you go? You can look for a forest or a outpost. {F/OP} """)

if crossroad1.upper().strip() == "F":
    crossroad2 = input("""
You go to the forest. You can chop down some trees or go hunting. {T/H}""" )

    if crossroad2.upper().strip() == "T":
        print("""
While chopping down trees a tree falls on top of you... You die! Ending 1/8...""") #ending 1/8

    elif crossroad2.upper().strip() == "H":
        crossroad3 = input("""
You find a bear. Will you attack or run away{ATK/RUN}""")

        if crossroad3.upper().strip() == "ATK":
           print(""" 
You try to attack a bear with a stick, it brutally devours you... You die 2/8...""")  #ending 2/8

        elif crossroad3.upper().strip() == "RUN":
            crossroad4 = input("""
You run away, you can head home or keep hunting.{HOME/HUNT}""")

            if crossroad4.upper().strip() == "HOME":
                semicross1 = input("""
You find a deer on your way home. Take it or leave it? {TAKE/LEAVE}""")

                if semicross1.upper().strip() == "TAKE":
                    print("""
You take the deer home and feed yourself YOU WIN! Ending 3/8...""") #ending 3/8

                elif semicross1.upper().strip() == "LEAVE":
                    print("""
You get so hungry you cant walk any longer, you get eaten by wolves... You die! Ending 4/8... """) #ending 4/8

            elif crossroad4.upper().strip() == "HUNT":
                print("""
As you are heading home it gets dark, you are eaten by wolves... You die! Ending 5/8 """) #ending 5/8

if crossroad1.upper().strip() == "OP":
    opcrossroad1 = input("""
You look for a outpost... Which do you go to the valley or deeper into the woods? {V/W}""")

    if opcrossroad1.upper().strip() == "V":
        opcrossroad2 = input("""
As you almost reach the outpost a pack of wolves get in your way... Run or attack? {RUN/ATK}""")

        if opcrossroad2.upper().strip() == "ATK":
            print("""
You attack the pack of wolves with a stick, they bite you limb from limb... You die! 6/8""") #ending 6/8

        elif opcrossroad2.upper().strip() == "RUN":
            opcrossroad3 = input("""
You get to the outpost and get really hungry and you want some food... You only have $15 and the food cost $12, do you buy it? {Y/N}""")

            if opcrossroad3.upper().strip() == "Y":
                opcrossroad4 = input("""
You buy some food and head home, as you are going home an angry bear trys to steal your food! Attack or run! {ATK/RUN}""")

                if opcrossroad4.upper().strip() == "ATK":
                    print("""
You attack the bear, you hit the bear and it runs off, afterwards you make it home safetly! You win! Ending 7/8""")

                elif opcrossroad4.upper().strip() == "RUN":
                    print("""
The bear chases you and you fall, the bear eats you and the food. Ending 8/8""") #ending 8/8

    elif opcrossroad1.upper().strip() == "W":
        print("""
As you go to the woods it gets colder and you get hungry, as you reach into your bag you notice that you have no food! Your starve... You die!""")