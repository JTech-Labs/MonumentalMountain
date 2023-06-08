import sys, time, random, os, webbrowser


    #Some Variables
inventory = str("_")
health = int(100)
protection = int(0)
power = int(1)
magic = int(0)
sh1 = int(0)
fight1_2 = int(1)
TimeSleep = float(0.05)

    #Definitions
def PlayerStatus():
    print('\n')
    print(f"\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n")
    print('\n')

def stop_all():
    print(f"Input invalid, sorry {name}, you lose...")
    time.sleep(5)
    quit()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(TimeSleep)
