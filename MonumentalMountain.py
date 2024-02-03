from modules import health,protection,power,magic,inventory,clear,printSlow,msg,vowels,PowerUps,HashPassword
from story import places,msgs,compassMsgs,NPCmsgs,secMsgs,Items
from intro import intro
clear()

introchoice = input("Would you like the introduction [Y/n]?:\t").title()
if introchoice == "Y" or introchoice == "Yes": name = intro()
else:
    name = input("You decide to refer to yourself as:\n>")
    print('\n')


currentRoom = "Superliminal Space"

TFmsgs = not True

while True:
    
    ## Start Turn
    
    clear()
    printSlow(f"{msg}\n\n")
    
    if TFmsgs == True:
        printSlow(msgs[currentRoom])
        print('\n'*2)
    
    if health <= 0:
        printSlow("Your health is 0 or less. You died.")
    
    if power < 0:
        power = 0
    
    if protection < 0:
        protection = 0
    
    if magic < 0:
        magic = 0
    
    ## Place Checkers

    # Item indicator
    if "Item" in places[currentRoom].keys():

        nearbyItem = places[currentRoom]["Item"]

        if nearbyItem not in inventory:

            if nearbyItem[-1] == 's' or nearbyItem == "Sand":
                printSlow(f"You see {nearbyItem}")

            elif nearbyItem[0] in vowels:
                printSlow(f"You see an {nearbyItem}")

            else:
                printSlow(f"You see a {nearbyItem}")
            print('\n')

    #Boss Checker
    if "Boss" in places[currentRoom].keys() and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
        printSlow(f"You see a Boss {places[currentRoom]['Boss']}!\n")
    
    #NPC Checker
    if "NPC" in places[currentRoom].keys():
        printSlow(f"You see an NPC {places[currentRoom]['NPC']}\n")

    #Sign Chcker
    if "NPCS" in places[currentRoom].keys():
        printSlow(f"You see a sign {places[currentRoom]['NPCS']}\n")


    #Power Up checker
    if "PU" in places[currentRoom].keys():
    
        PowerUp = places[currentRoom]["PU"]

        if currentRoom not in PowerUps:
            PowerUps.append(currentRoom)
            health += places[currentRoom]["PU"]["Health"]
            protection += places[currentRoom]["PU"]["Protection"]
            power += places[currentRoom]["PU"]["Power"]
            magic += places[currentRoom]["PU"]["Magic"]

    #Secret Checker
    if "Secret" in places[currentRoom].keys():
        if f"{places[currentRoom]['Secret']}s" not in PowerUps:
            realname = input("Please enter your real name:\n>")
            realnameHash = HashPassword(realname)
            print(realnameHash)
            if  realnameHash in places[currentRoom]['Secret']:
                print(secMsgs[currentRoom][realnameHash[-2:]])
            else: clear()
            PowerUps.append(f"{places[currentRoom]['Secret']}s")

    ## Player Moves

    # Accepts player's move as input
    userInput = input("\n\nEnter your move:\n> ")

    # Splits move into words
    nextMove = userInput.split(' ')

    # First word is action
    action = nextMove[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(nextMove) > 1:
        item = nextMove[1:]
        direction = nextMove[1].title()
        item = " ".join(item).title()
    

    # Moving between places
    if action == "Go":

        try:
            currentRoom = places[currentRoom][direction]
            msg = f"You go {direction}"

        except:
            msg = "You can't go that way."

    # Picking up items
    elif action == "Get":
        try:
            if item == places[currentRoom]["Item"]:

                if item not in inventory:

                    inventory.append(places[currentRoom]["Item"])
                    msg = f"{item} retrieved!"
                    health += Items[item]["Health"]
                    protection += Items[item]["Protection"]
                    power += Items[item]["Power"]
                    magic += Items[item]["Magic"]

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    #Player Statistics and Inventory
    elif action == "Stats":
        msg = f"\n\n{name}:\n\t Inventory: {inventory} \n\t Health: {health} \n\t Protection: {protection}\
\n\t Power: {power} \n\t Magic: {magic} \n\n"
    

    # Gives the compass messages
    elif action == "Compass":
        if "Compass" in inventory:
            try:
                msg = compassMsgs[currentRoom]
            except:
                msg = 'There is no message for this place'
        else: msg = "You don't have a Compass."
    
    #Displays Help message with all available functions
    elif action == "Help":
        msg = "Possible actions:\n\tLook: Repeat prompt\n\tCompass: Get extra help if you need it\
\n\tStats: Print your stats\n\tHelp: Prints this\n\tYou can \"Go\":\n\t\tForewards\n\t\tBack\n\t\t\
Left\n\t\tRight\n\tYou can \"Get\" the item in the room that you are in if you don't already have it.\n\t\
You can \"Drop\" an item you have in your inventory\n\tYou can \"Speak\" or \"Talk\" [Name of NPC] to talk with a Non-Playable Character, \
Do not use anything apart from initial keyword and the name of the NPC (This also works with bosses).\n\t\
You can \"Fight\" a boss in the room you are in\n\tAnd you can always \"Exit\"\n"
    
    #Reprints the current room message 
    elif action == "Look":
        TFmsgs = True
        continue

    #Talk with characters, NPCs or Bosses
    elif action == "Talk" or action == "Speak":
        if 'NPC' in places[currentRoom].keys():
            if item == places[currentRoom]['NPC']:
                msg = NPCmsgs['NPC'][item]['Conv']
            else: msg = f"Can't find \"{item}\" here."

        #Remember to add powerupps to NPCs if applicable
        elif 'Boss' in places[currentRoom].keys():
            if item == places[currentRoom]['Boss']:
                msg = NPCmsgs['NPC'][item]['Conv']
            else: msg = f"Can't find \"{item}\" here."
        
        else: print("There is no one to talk to here.")

   #Read signs 
    elif action == "Read":
        if 'NPCS' in places[currentRoom].keys():
            if item == places[currentRoom]['NPCS']:
                msg = NPCmsgs['NPCS'][item]['Tex']
            else: msg = f"Can't find the sign \"{item}\" here."
        else: print("There are no signs here.")
   

    #Fight Bosses
    elif action == "Fight":
        if "Boss" in places[currentRoom]:
            if f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][0] <= health and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][1] <= protection and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][2] <= power and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][3] <= magic and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][4] in inventory:
                    PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                    msg = {NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["FightWin"]}

                    PowerUps.append(currentRoom)
                    health += places[currentRoom]["PU"]["Health"]
                    protection += places[currentRoom]["PU"]["Protection"]
                    power += places[currentRoom]["PU"]["Power"]
                    magic += places[currentRoom]["PU"]["Magic"]

                else:
                    msg = f"{NPCmsgs['Bosses'][places[currentRoom]['Boss']]['FightLose']}\nYour stats didn\'t meet the requirements to beat this Boss"

            else: msg = "You have allready fought this boss and they have despawned."
               
    elif action == "Drop":
        try:
            inventory.remove(item)
            msg = f"{item} has been removed from your inventory, you can retrieve it back from where you found it."
        except:
            msg = f"You dont have that item"

    
    ##Debug commands
    #Prints your current room
    
    elif action == "Where":
        msg = currentRoom

    #Changes option if you want ot see the current room message or not
    elif action == "Chngmsgs":
        TFmsgs = not TFmsgs
        msg = ''

    #Change printSlow speed
    elif action == "Sped":
        sped = float(item)

    #Teleport
    elif action == "Tp":
        if item in places.keys():
            currentRoom = item
            msg = f'You are in {currentRoom}'
        else: msg = "No such place"

    elif action == "Pu":
        msg = PowerUps

    # Exit program
    elif action == "Exit":
        clear()
        printSlow('You have left the realm, see you later!')
        quit()

    # Any other commands invalid
    else:
        msg = "Invalid command\n"
