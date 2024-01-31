#Improts
import sys, time, os
# from story import NPCconvers

#Stats
health = 100
protection = 0
power = 0
magic = 0
inventory = []

#Functions
# def playerStatus():
#     print(f"\n\nYou are: {name}. These are your stats\n\n Inventory: {inventory} \n Health: {health} \n\
#          Protection: {protection} \n Power: {power} \n Magic: {magic} \n\n")

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

# Function used to print the text as if it where being typed
def printSlow(stri):
    for letter in stri:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

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

def npc():
    print("Not yet implemented.")

vowels = ['a', 'e', 'i', 'o', 'u']

msg = ""