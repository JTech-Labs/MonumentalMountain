<!--
SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>

SPDX-License-Identifier: MIT
-->

# Intro
This file is for reference purposes only and is used to document all the Features, Bosses, NPCs, Items and the basic system of the main game

---

MonumentalMountain uses several systems to keep track of Bosses, NPCs, the player Inventory and several other stats. Most use dictionaries, variables or lists. This document is purely to note down what each thing does and is, so the devs can keep track and the players can use it as a reference point. If you have any questions, please open an issue.

---
## Stats
Stats are different values that tell you about how your character is.

- Inventory -> These are all the items you have
- Health -> Also known as HP is the amount of health points you have with a maximum of 100
- Power -> 

---
## Commands
There are a lot of commands you can use. And a few secret and debug ones you can use ;)
All commands are in format:
Command Parrameter (parrameters are shown in brackets [], but you don't write them in the actual command)

### Main
- Look -> Repeat room message
- Compass -> Get extra help if you need it
- Stats -> Print your current Stats (Inventory - Health - Protection - Power - Magic)
- Help -> Prints a quick help message
- Go:
    - Forwards -> Move forewards
    - Backwards -> Move Backwards ("Back" also works)
    - Left -> Move Left
    - Right -> Move Right
- Get [item] -> Inserts any item in the current room into your inventory if it is either stackable or you don't have it
- Drop [item] -> You drop any item in your inventory (you can find it again in the room you found it)
- Use [item] -> Use or consume any item in your inventory\n\t\
- Speak/Talk [character] -> Talk with any NPC or boss
- Fight [Boss or enemy] -> Engage in fight with an enemy or boss
- Whatis [item]  -> Gets the description of an item in your inventory

And you can always "Exit"

### Debug
- Chngmsgs -> Toggles there being a message for each room you are in, useful if you want to quickly move around
- Where -> Displays the current room you are in

(Plus a few secret commands! Although you could just find them in the source code :D)

---
## Items
These are the things that are added to your inventory, they can give you buffs (Power Ups) and have special uses.

Not Yet Implemented ==> There are several rarity levels out of 100. The higher the rarity, the better the item (normally).

### Non-Use
These are items that you always carry with you but you can't use directly

- SpecialTorch -> Lets you see in darker places (allows you to access more places)
- Coin -> Lvl - 1. Buffs: +2 Health, +2 Protection and +1 Magic. A small golden disk ressembling what you know as a coin, belonging to a long forgoten civilication. It holds a special power and a surge of positive, warm energy shoot up your body when you touch it
- Sand -> Utterly useless, reduces health and power. Basically extra weight

### Multi-Use
These Items you can pick up and use as many times as you want (if it can be used), the buffs they give you are only applicable while you have it. You can drop it and pick it back up from where you first found it.

__*!!ATTENTION!!*__ If for example you have an item that buffs you ten points and then you drop the item when you have less than this e.g. 9HP, then you will still lose the same amount you gained when you picked it up, so you will die. So be careful. Overall, it is a beter idea not to drop Multi-Use items, specially if you have very low stats.

* Compass -> Lvl - 3.Gives you tips on the best move available. Although it sometimes might tell you a bit of information, and can always just not say anything at any given place.
* Wand -> Lvl - 80. Buffs: +50 Health, +50 Protection, +90 Power, +30 Magic

### Single-Use
These Items you can pick up and use only once (mostly single boosts, like food or potions). You can drop these but they will break on the floor and you won't be able to get them back.

- Bread Loaf -> Buffs: +5 Health, +2 Power
- WhackyPotion -> Random effects for all stats with a change between 5 and -5
- RedPotion -> Buffs: +20 Health, +7 Power
- BreadLoaf -> Buffs: +5 Health, +2 Power