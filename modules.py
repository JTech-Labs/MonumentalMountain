#Improts
import sys, time, os, hashlib

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

vowels = ['a', 'e', 'i', 'o', 'u']

msg = ""