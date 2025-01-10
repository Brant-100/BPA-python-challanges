import random

# Starting attributes


'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


A monster is attacking you!
Enter:  '1' to use your ___
        '2' to run away
Choice: ___
You defeated the monster and found ___!
That was rough! You lost ___ health.
Luckily you managed to get past the monster!
Press Enter to continue
___ gold
a health potion. You restored ___ health
Hello, ___
In this dungeon, you will fight three monsters.
If you survive to the end, treasure awaits!
You have your trusty ___, I see.
Good. You will need it.
Press Enter when you are ready to begin...
You made it to the treasure! You found ___ gold!
You didn't find the treasure, but you survived to fight again another day...
You fought as best you could, but didn't make it. 
The treasure waits for the next adventurer...
'''

# Write your functions here


def start_game():
    global name
    global weapon

    print("Welcome to the dungeon!")

    name = input("What is your name, adventurer?:  ")

    weapon = input("What is your weapon of choice? ")

    display_character()
    print(f"Hello, {name}! in this dungen, you will fight three monsters. If you survive to the end, treasure waits! tou have your trust{weapon}, I see good you will need it. ")
    input ("press enter when your ready to begin....")
    encouter_monsters()
    

def display_character():
    # Finish this function here
        global health
        global gold
        global strength
        global name
        global weapon
        global level 
        health = random.randint(7,10) * 10
        gold = 0
        strength = random.randint(12,17)
        level = 1

        print(f"name:{name}                                       level:{level}")
        print (f"gold: {gold}                                      weapon:{weapon}")
        print (f"health:{health}                                   strength: {strength}")

def find_loot():
    global level
    global items_to_be_found_hi
    gold_find = random.randint(25,150)
    health_find = random.randint(10,30)
       
    items_to_be_found = ("gold", "health")
    items_to_be_found_hi = random.choices(items_to_be_found, weights=(70,30))
    if items_to_be_found == "gold":
            print(f"you found {gold_find} gold")
    elif items_to_be_found == health:
            print (f"you found a health potion restoreing {health_find}")
    else:
            print("sorry chump you aint find notin")

            gold_find =+ gold
            health_find =+ health
            level =+ 1
            display_character()
            input("lets contuinue on the jurney (press enter): ")
def encouter_monsters():
    global choice
    global action
    global monsters_killed
    global win
    global m_strength
     
    choice = print("A monster is attacking you!!")
    action = input (f"enter: '1' to use your {weapon} '2' to run away: ")
    
    if action == '1':
        win = (f"this monster has {m_strength}")
        if win < {strength}:
              pass
        elif win > {strength}:
              dps = print (f"sorry you just took {m_strength} * 10" damage)
              health - dps

        
        print(f"you Obliterated the monster with your might {weapon}")
        find_loot()
    elif action == '2':
          print (f"you ran away like a scared little baby you {weapon} felt limp in your hands")
    else:
          print("sorry invlaid input")
    input("lets see your loot (press enter): ")
    monsters_killed = 0
    while monsters_killed <= 3: 
          break
    monsters_killed =+ 1 
    

    find_loot()
    
class monster():
      
      m_strength = random.randint(13, 18)


start_game()