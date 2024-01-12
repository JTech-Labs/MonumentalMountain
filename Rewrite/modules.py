#Improts
import sys, time, os

#Stats
health = 100
protection = 0
power = 0
magic = 0
inventory = []

    #Functions
def PlayerStatus():
    print(f"\n\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n\n")

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def printSlow(stri):
    for letter in stri:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)

places = {
    'Superliminal Space': {'Forewards': 'Mountain Base', 'Right': 'Forrest', 'Left': 'Dessert'},
    'Dessert Start': {'Forewards': ''}
}

msgs = {
    'Superliminal Space': "",
}

vowels = ['a', 'e', 'i', 'o', 'u']

msg = ""