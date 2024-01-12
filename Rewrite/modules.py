#Improts
import sys, time, random, os, webbrowser

def PlayerStatus():
    print(f"\n\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n\n")

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def printSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(TimeSleep)


places = {
    'Superliminal Space': {'Forewards': 'Mountain Base', 'Right': 'Forrest', 'Left': 'Dessert'},
    'Dessert Start': {'Forewards': ''}

}

msgs = {
    'Superliminal Space': "",
    
}

vowels = ['a', 'e', 'i', 'o', 'u']

inventory = []

msg = ""

