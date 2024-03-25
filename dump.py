
def stillunderdevelopment():
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


