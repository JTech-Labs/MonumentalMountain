#Improts
import sys, time, os, hashlib
# from story import NPCconvers

#Stats
health = 100
protection = 0
power = 0
magic = 0
inventory = [""]
PowerUps = [""]

#Functions
# def playerStatus():
#     print(f"\n\nYou are: {name}. These are your stats\n\n Inventory: {inventory} \n Health: {health} \n\
#          Protection: {protection} \n Power: {power} \n Magic: {magic} \n\n")

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

# line_len_limit = 80

# def pr0intSlow(text):
#     words = text.split(' ')    
#     line = ''
#     for i, word in enumerate(words):
#         if len(line) + len(word) < line_len_limit:
#             line += f'{word} '
#         else:
#             slowPrint(line)
#             if len(word) >= line_len_limit:
#                 slowPrint(word)
#                 return(printSlow(' '.join(words[i+1:]), line_len_limit))
#             return(printSlow(' '.join(words[i:]), line_len_limit))


def HashPassword(password):
    # Encode the password as bytes
    passwordBytes = password.encode('utf-8')
    
    # Use SHA-256 hash function to create a hash object
    hashObject = hashlib.sha256(passwordBytes)
    
    # Get the hexadecimal representation of the hash
    passwordHash = hashObject.hexdigest()
    
    return passwordHash

def npc():
    print("Not yet implemented.")

vowels = ['a', 'e', 'i', 'o', 'u']

msg = ""