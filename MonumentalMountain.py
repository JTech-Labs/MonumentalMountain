import sys,time,random
# This is MonumentalMountain Aplpha v0.0.1
# This "Alpha Game Programm" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licenced under the GNU GPLv3 licence by GAMAX-INTERACTIVE, part of the JAI-INNOVATIONS
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Welcome to MonumentalMountain Alpha v0.0.1. Created by GAMAX-INTERACTIVE")
print("")

print_slow("Legends have been told about the Mysterious Monumental Mountain, a realm only accessible though sleep in very specific circumstances.")
print("")

print_slow("A place made at the begining of humanity by the supreme planetary council of intelligence to test humankind until they are balanced enough as a species to join the coulcil")
print("")

print_slow("You, a simple human who have only read about these things in medieval library books, go to bed in peace without the knowledge that exactly at midnight of the summer equinox of 2023 eveyone on the dark and light side of the Erath unconciously decide to sleep all at the same time.")
print("")

print_slow("Only the human that is most conciously unprepared by subconciously ready that would be chosen to go and stand for their species.")

print_slow("And that one specific person, this one specific time happens to be...")
print_slow("You")

print("")
print("")
print("")

name = input("Welcome! Who is the lucky adventurer we have this cerntury?:    ")
print("Welcome", name, "to the Monumental Mountain. We will lead you through the terrain and youu have to make decisions as you go along and please ansewer in all lowercase.")

yesno1 = input("Are you ready?")
yes = ("yes")
no = ("no")

if yesno1 == "yes":
    typing_speed = 50
    def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/typing_speed)
        print ('Starrting . . . . .')
else:
    quit()
