import random



# Global variables
name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0


def display_status():
    print (f"medic {name} has {medical_supplies} medical supplies, {energy} energy, and has treated {ewoks_treated} Ewoks.")


def treat_ewok():
    global medical_supplies
    global energy
    global ewoks_treated
    global name

    display_status()
    condition = random.choice(["Minor", "Moderate", "Severe"])
    ewok_condition = print(f"The Ewok's condition is {condition}.")
  
    if medical_supplies >= 0 or energy >= 0:
        print("You don't have enough supplies to treat the Ewok.")
        end_shift()   
 
    if condition == "Minor":
        medical_supplies -= 5
        energy -= 5
        ewoks_treated += 1
        print(f"You treated the Ewok's minor injuries. by slapping a bandaid on it, and used {medical_supplies} medical supplies and {energy} energy.")
        encounter_ewok()
   
    elif condition == "Moderate":
        medical_supplies -= 15
        energy -= 10
        ewoks_treated += 1
        print(f"You treated the Ewok's moderate injuries. By giving it a splint , and used {medical_supplies} medical supplies and {energy} energy")
        encounter_ewok()
   
    elif condition == "Severe":
        medical_supplies -= 30
        energy -= 15
        ewoks_treated += 1
        print(f"You treated the Ewok's severe injuries.By giving it a blood transfusion, and used {medical_supplies} medical supplies and {energy} energy")
        encounter_ewok()


    
def start_shift():
    """
    Starts the shift and runs encounters with Ewoks.
    """
    global name
    print("Welcome to the forest moon of Endor!")
    name = input("Enter your name, Medic: ")
    print(f"Welcome, Medic {name}. Ewoks are depending on you.")
    input("Press Enter when ready to begin your shift...")
   
    for _ in range(3):
        
        display_status()
        treat_ewok()
        end_shift()
        


def encounter_ewok():
    """
    Simulates an encounter with an injured Ewok.
    """
    global medical_supplies
    print("An injured Ewok needs your help!")
    while True:
        try:
            for _ in range(3):
                if medical_supplies <= 0 or energy <= 0:
                 break
            print("1. Treat the Ewok")
            print("2. Skip")
            choice = int(input("Choose an option: "))
            if choice == 1:
                    treat_ewok()
            elif choice == 2:
                    break
            else:
                    print("Invalid choice. Try again.")
      
        except ValueError as e:
            print(e)
    pass


def end_shift():
    """
    Ends the shift with a summary of the medic's performance.
  print ("-------------------------------------")  """
    if ewoks_treated == 3:
     print(f"you did great {name}")
    elif ewoks_treated == 2:
      print(f"you did okay {name}")
    elif ewoks_treated == 1:
        print(f"you bad today {name} you need to use more supplise to help more ewoks")

# Start the shift
start_shift()
