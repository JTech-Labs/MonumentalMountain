# SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
#
# SPDX-License-Identifier: MIT

#Improts
import sys, time, os, hashlib, json
from os.path import isfile

#Stats
health = 100
protection = 100
power = 100
magic = 100
inventory = ["", 'Special Torch', 'Coin', 'Wand']
PowerUps = []

## Remember to add this later
#mainHand = [""]

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

# Function used to print the text as if it where being typed

sped = 0.05

def printSlow(stri):
    for letter in stri:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(sped)

def HashPassword(password):
    # Encode the password as bytes
    passwordBytes = password.encode('utf-8')
    
    # Use SHA-256 hash function to create a hash object
    hashObject = hashlib.sha256(passwordBytes)
    
    # Get the hexadecimal representation of the hash
    passwordHash = hashObject.hexdigest()
    
    return passwordHash

def getStory():
    got = False

    while not got:
        print("Please input your prefered language as a ISO 639 language code (e.g. `en`, `es` or `eo`)")
        lang = input("\n>")
        
        for i in range(len(lang)):
            if lang[i] not in alphabet:
                print("Language code must have only letters in the English alphabet, try again")
                continue

        if len(lang) > 2 or len(lang) < 2:
            print("Language code must be exactly two characters long, try again")
        
        if not isfile(f"story/{lang}.json"):
            print("That language is currently not implemented, you can try another or contribute if you want!")

        else:
            got = True

    with open(f'story/{lang}.json') as f:
        lang = json.load(f)
    
    if lang["test"]:
       print(lang["name"])
    else:
        print("ERROR!!:  Couldn't load language for an unexpected reason!\n\t\t\t\tPlease try again")
    
    story = lang["STORY"]
    ui = lang["UI"]
    introText = lang["INTRO"]

    return story, ui, introText
        
alphabet = "abcdefghijklmnopqrstuvwxyz"


msg = ""
