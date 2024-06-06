from modules import *
from story import *
from intro import intro
import linecache
##from dump import stillunderdevelopment
# This is MonumentalMountain Alpha v0.0.4
# This "Alpha Game Program" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licensed under the GNU GPLv3 license by ?, part of the J-A-I INNOVATIONS

#Define Items

#Setup the game and intro
def gameSetup():
    clear()


    introchoice = input("Would you like the introduction [Y/n]?:\t").title()
    if introchoice == "Y" or introchoice == "Yes": name = intro()
    else:
        name = input("You decide to refer to yourself as:\n>")
        print('\n')

    timer = 0

    TFmsgs = not True

    return name, timer, TFmsgs

#Main function
if __name__ == "__main__":
    #Run Game Setup and initiate variables
    name,timer,TFmsgs = gameSetup()
    
    #Main game loop
    while True:
        
        ## Start Turn
        #Clear Screen
        clear()

        #Display death message if health is zero or less
        if health <= 0:
            printSlow("Your health is 0 or less. You died.\n\nThanks for playing. You can always replay if you want, but your progress will not have been saved.")
            quit()

        printSlow(f"{msg}\n\n")
        
        #This part slowly lowers your power and health as time passes, forcing you to eat and drink
        timer += 1
        if timer == 10:
            power -= 1
        if timer == 20:
            health -=1
            power -=1
            timer = 0
        
        #Health Warnings        
        if health <= 50 and health >= 45:
            printSlow("Your health is a bit low, you might want to heal by using a food or drink.\n")
        if health <= 40 and health >= 30:
            printSlow("Your health is quite low, you might want to heal by using a food or drink.\n")
        if health <= 10 and health >= 0:
            printSlow("Your health is very low, it is recomended that you heal as quick as possible.\n")

        #Print Room message unless option is turned off
        if TFmsgs:
            
            with open("story.txt","r") as fi:
                for ln in fi:
                    if ln.startswith(currentRoom):
                        printSlow(ln.partition(': ')[-1])
                        break

            print('\n'*2)
        
        #Reset Buffs to zero if they are less than that
        if health > 100:
            health = 100
        
        if power < 0:
            power = 0
        
        if protection < 0:
            protection = 0
        
        if magic < 0:
            magic = 0
        
        ## Place Checkers

        # Item indicator
        if "Item" in places[currentRoom]:
                
                for theItemsInTheRoom in range(places[currentRoom]["Item"]):

                    nearbyItem = places[currentRoom]["Item"][theItemsInTheRoom]

                    if nearbyItem not in inventory and f"{currentRoom}-{nearbyItem}" not in PowerUps:

                        if nearbyItem[-1] == 's' or nearbyItem == "Sand":
                            printSlow(f"You see {nearbyItem}")

                        elif nearbyItem[0] in vowels:
                            printSlow(f"You see an {nearbyItem}")

                        else:
                            printSlow(f"You see a {nearbyItem}")
                        print('\n')
        else: continue

        #Boss Checker
        if "Boss" in places[currentRoom] and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
            printSlow(f"You see a Boss: {places[currentRoom]['Boss']}!\n")
        
        #NPC Checker
        if "NPC" in places[currentRoom]:
            printSlow(f"You see an NPC {places[currentRoom]['NPC']}\n")

        #Sign Chcker
        if "NPCS" in places[currentRoom]:
            printSlow(f"You see a sign {places[currentRoom]['NPCS']}\n")

        #Secret Checker
        if "Secret" in places[currentRoom]:
            if f"{places[currentRoom]['Secret']}s" not in PowerUps:
                realname = input("Please enter your real name:\n>")
                realnameHash = HashPassword(realname)
                #print(realnameHash)
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
            if direction == "Back":
                direction = "Backwards"
            try:
                currentRoom = places[currentRoom][direction]
                #Each room can have a required item to pass, otherwise it will appear as if that isn't an available path
                if 'Req' in places[currentRoom]:
                    if places[currentRoom]['Req'] in inventory:
                        msg = f"You go {direction}"
                    else:
                        msg = "You can\'t go that way"
                        currentRoom = places[currentRoom]['Backwards']
                else: msg = f"You go {direction}"

            except KeyError:
                msg = "You can't go that way."

        # Picking up items
        elif action == "Get":
            try:
                if item in places[currentRoom]["Item"]:

                    if item not in inventory:
                        
                        if item.split() > 1: item = "".join(item.split())

                        inventory.append(item)


                        msg = f"{item} retrieved!"

                        if item.canBeUsed:
                        
                            if item.singleUse:
                                PowerUps.append(f"{currentRoom}-{nearbyItem}")
                            elif not item.singleUse:
                                health += item.Health
                                protection += item.Protection
                                power += item.Power
                                magic += item.Magic
                        else:
                            health += item.Health
                            protection += item.Protection
                            power += item.Power
                            magic += item.Magic

                    else:
                        msg = f"You already have the {item}"
                
                else:
                    msg = f"Can't find {item}"
            except KeyError:
                msg = f"Can't find {item}"
        
        #Player Statistics and Inventory
        elif action == "Stats":
            msg = f"\n\n{name}:\n\t Inventory: {inventory} \n\t Health: {health} \n\t Protection: {protection}\
    \n\t Power: {power} \n\t Magic: {magic} \n\n"
        

        # Gives the compass messages
        elif action == "Use" or action == "Eat":
            
            if item == "Compass":
                with open("story.txt","r") as fi:
                    for ln in fi:
                        if ln.startswith(f"C- {currentRoom}"):
                            compassMsg = ln.partition(': ')[-1]
                            break

            if item in inventory:
                if item.canBeUsed:
                    if item.msgt:
                        msg = item.msg
                    else: msg = ''
                    if item.singleUse:
                        inventory.remove(item)
                        PowerUps.append(item)
                        health += item.Health
                        protection += item.Protection
                        power += item.Power
                        magic += item.Magic
                else: msg = "You can't use that item"
            else: msg = f"You don't have the item \"{item}\""
        
        #Displays Help message with all available functions
        elif action == "Help":
            msg = "Possible actions:\n\tLook: Repeat prompt\n\tCompass: Get extra help if you need it\
    \n\tStats: Print your stats\n\tHelp: Prints this\n\tGo:\n\t\tForwards\n\t\tBackwards\n\t\t\
    Left\n\t\tRight\n\tGet: [The item you want if you don't already have it].\n\t\
    Drop: [Any item in your inventory]\n\tUse: [An Item in your inventory(if it is usable, use this instead of eat or drink)]\n\t\
    Speak/Talk: [Any NPC or character in that room (, \
    Do not use anything apart from initial keyword and the name of the NPC (This also works with bosses)).\n\t\
    Fight: [The boss in the room you are in]\n\tWhatis: [item] Gets the description of an item in your inventory\n\tAnd you can always \"Exit\"\n\nIf you need more help, plese see Features.md"
        
        #Reprints the current room message 
        elif action == "Look":
            TFmsgs = True

        #Talk with characters, NPCs or Bosses
        elif action == "Talk" or action == "Speak":
            if 'NPC' in places[currentRoom]:
                if item == places[currentRoom]['NPC']:
                    #Check if the player can continuously speak with an NPC
                    if not f"NPCPU{item}" in PowerUps: # Remember to apply """ NPCmsgs['NPC'][item][5] """ for multiple different dialouges
                        # Get the Dialogue form the story.txt file
                        with open("story.txt","r") as fi:
                            for ln in fi:
                                if ln.startswith(f"NPC- {item}"):
                                    msg = ln.partition(': ')[-1]
                                    break
                    else:
                        msg = f"{item} is no longer here"
                    # Check if the player has already had a conversation with the NPC
                    if f"NPCPU{item}" not in PowerUps:
                        health += NPCmsgs['NPC'][item][0]
                        protection += NPCmsgs['NPC'][item][1]
                        power += NPCmsgs['NPC'][item][2]
                        magic += NPCmsgs['NPC'][item][3]
                        for itemAmount in NPCmsgs['NPC'][item][4]:
                            if NPCmsgs['NPC'][item][4][itemAmount] not in inventory:
                                inventory.append(NPCmsgs['NPC'][item][4][itemAmount])
                        PowerUps.append(f"NPCPU{item}")
                    else:
                        ''

            elif 'Boss' in places[currentRoom]:
                if item == places[currentRoom]['Boss']:
                    if f"NPCPU{item}" in PowerUps:
                        with open("story.txt","r") as fi:
                            for ln in fi:
                                if ln.startswith(f"NPC- {item}-A"):
                                    msg = ln.partition(': ')[-1]
                                    break
                    
                    elif f"{places[currentRoom]['Boss']}bw" in PowerUps:
                        msg = f"You have slain {item}"

                    else:
                        with open("story.txt","r") as fi:
                            for ln in fi:
                                if ln.startswith(f"NPC- {item}"):
                                    msg = ln.partition(': ')[-1]
                                    break
                    if NPCmsgs['NPC'][item]:
                        if f"NPCPU{item}" not in PowerUps and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                            health += NPCmsgs['NPC'][item][0]
                            protection += NPCmsgs['NPC'][item][1]
                            power += NPCmsgs['NPC'][item][2]
                            magic += NPCmsgs['NPC'][item][3]
                            for itemAmount in NPCmsgs['NPC'][item][4]:
                                if NPCmsgs['NPC'][item][4][itemAmount] not in inventory:
                                    inventory.append(NPCmsgs['NPC'][item][4][itemAmount])
                            PowerUps.append(f"NPCPU{item}")
                else: msg = f"Can't find \"{item}\" to talk to here."
            else: msg = f"Can't find \"{item}\" to talk to here."

       #Read signs 
        elif action == "Read":
            if 'NPCS' in places[currentRoom].keys():
                if item == places[currentRoom]['NPCS']:
                    msg = NPCmsgs['NPCS'][item]['Tex']
                else: msg = f"Can't find the sign \"{item}\" here."
            else: print("There are no signs here.")

        #Fight Bosses or Enemys
        elif action == "Fight":
            try:
                if "Boss" in places[currentRoom]:
                    if item == places[currentRoom]['Boss']:
                        if f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                            
                            doYouhavethatitem = True
                            doYouhavethatitemNum = 0
                            for doYouhavethatitemNum in range(NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4]):
                                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4][doYouhavethatitemNum] not in inventory:
                                    doYouhavethatitem = False
                                    break
                                else:
                                    continue
                            if doYouhavethatitem:
                                                    
                                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][0] <= health and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][1] <= protection and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][2] <= power and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][3] <= magic:
                                    # Add support for several required items
                                    for gotThatItem in NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4]:

                                        PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                                        with open("story.txt","r") as fi:
                                            for ln in fi:
                                                if ln.startswith(f"Enemy- {item}-W"):
                                                    msg = ln.partition(': ')[-1]
                                                    break

                                        PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                                        health += NPCmsgs['Bosses'][item]['Effects']["Health"]
                                        protection += NPCmsgs['Bosses'][item]['Effects']["Protection"]
                                        power += NPCmsgs['Bosses'][item]['Effects']["Power"]
                                        magic += NPCmsgs['Bosses'][item]['Effects']["Magic"]
                                        # Add support for several dropped items
                                        for gotThatItemNum in range(len(NPCmsgs['Bosses'][item]['Effects']['Item'])):
                                            if NPCmsgs['Bosses'][item]['Effects']["Item"][gotThatItemNum] not in inventory:
                                                inventory.append(NPCmsgs['Bosses'][item]['Effects']["Item"][gotThatItemNum])

                                else:
                                    with open("story.txt","r") as fi:
                                        for ln in fi:
                                            if ln.startswith(f"Enemy- {item}-L"):
                                                imsg = ln.partition(': ')[-1]
                                                break
                                    msg = f"{imsg}\nYour stats didn\'t meet the requirements to beat this Boss"
                            else:
                                with open("story.txt","r") as fi:
                                    for ln in fi:
                                        if ln.startswith(f"Enemy- {item}-L"):
                                            imsg = ln.partition(': ')[-1]
                                            break
                                msg = f"{imsg}\nYour stats didn\'t meet the requirements to beat this Boss"

                        else: msg = "You have already fought this boss and they have despawned."
                    else:  msg = f"Can't find \"{item}\" here."

            except KeyError: msg = f"There is no {item} here"


        elif action == "Drop":
            try:
                inventory.remove(item)
                
                if item.canBeUsed:
                    if item.singleUse:
                        msg = f"{item} has been removed from your inventory, it breaks on the ground and dissapears, you can\'t get it back from where you found it."
                    elif not item.canBeUsed:
                        health -= item.Health
                        protection -= item.Protection
                        power -= item.Power
                        magic -= item.Magic
                        msg = f"{item} has been removed from your inventory, you can retrieve it back from where you found it."
                        
                else:
                    health -= item.Health
                    protection -= item.Protection
                    power -= item.Power
                    magic -= item.Magic
                    msg = f"{item} has been removed from your inventory, you can retrieve it back from where you found it."

            except ValueError:
                msg = "You dont have that item"

        
        ##Debug commands
        #Prints your current room
        
        elif action == "Where":
            msg = currentRoom

        #Changes option if you want ot see the current room message or not
        elif action == "Chngmsgs":
            TFmsgs = not TFmsgs
            msg = ''

        ##Change printSlow speed
        #elif action == "Sped":
            #sped = float(item)

        #Teleport
        elif action == "Tp":
            if item in places:
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
