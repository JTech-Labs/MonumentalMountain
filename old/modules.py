# SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
# SPDX-FileCopyrightText: 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
# SPDX-FileCopyrightText: 2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
#
# SPDX-License-Identifier: MIT

import sys, time, random, os, webbrowser
from MonumentalMountain import name

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

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def stop_all():
    print(f"Input invalid, sorry {name}, you lose...")
    time.sleep(5)
    quit()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(TimeSleep)
