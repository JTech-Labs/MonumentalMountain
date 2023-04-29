import time, os

inventory = str("")
health = int(100)
protection = int(0)
power = int(1)
magic = int(0)

os.system('cls' if os.name == 'nt' else "printf '\033c'")

while True:
        print(f"\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")