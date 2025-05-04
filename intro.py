# SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
#
# SPDX-License-Identifier: MIT

import time,os,sys

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def printSlow(stri):
    for letter in stri:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

clear()

name = ""

#Intro
def intro(introText):
    
    for i in range(7):
        printSlow(introText[i])
    time.sleep(10)
    clear()

    for i in range(3):
        print(introText[i+7])

    yesno1 = input(introText[10])

    if yesno1 in introText[11]:
        print(introText[12][0])
    else:
        print(introText[12][1])
        quit()

    print(introText[13])
    print(introText[14])

    name = input(introText[15])

    print(f'{introText[16][0]}{name}{introText[16][1]}')

    print(introText[17])

    return name
