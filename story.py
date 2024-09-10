from random import randint

currentRoom = "Superliminal Space"

places = {
    'Superliminal Space': {'Forwards': 'Mountain Base', 'Right': 'Forrest Start', 'Left': 'Desert Start', 'Down': 'Tilled Land', 'msgs': 3, 'Item': ['Bread Loaf']},
    'Mountain Base': {'Backwards': 'Superliminal Space', 'Item': ['Whacky Potion'], 'msgs': 7},
    'Forrest Start': {'Backwards': 'Superliminal Space', 'Item': ['Wand'], 'msgs': 5},
    'Desert Start': {'Forwards': 'Desert Canyon', 'Right': 'Desert Shadow', 'Left': 'Desert Rocks', 'Backwards': 'Superliminal Space', 'Item': ['Bread Loaf']},
    'Tilled Land': {'Item': ['Compass']},
    'Desert Shadow': {'Backwards': 'Desert Start', 'Item': ['Coin']},
    'Desert Rocks': {'Secret': [
    "a0ead0b63e9ddc749106e77da630106b5be5d9a5c0be43e96098325f7ba9377d",
    "b743d651ac4a114940c1d141929b9ee08ad3c5cdc38e1d299bd307e4811639ae",
    "171886bac78f91b959d78a8679bffb1f94e23b82066f7a15f88e7b24b5ca9739"], 'Backwards': 'Desert Start', "Item": [""]},
    'Desert Canyon': {'Boss': 'Cocroach', 'Backwards': 'Desert Start', 'Item': ['Sand'], 'Forwards': 'Further Desert Canyon'},
    'Further Desert Canyon': {'Backwards': 'Desert Canyon', 'Req': 'Special Torch'}
}

secMsgs = {
    'Desert Rocks': {
        'b743d651ac4a114940c1d141929b9ee08ad3c5cdc38e1d299bd307e4811639ae': 'Welcome J-A-I',
        'a0ead0b63e9ddc749106e77da630106b5be5d9a5c0be43e96098325f7ba9377d': u'\u2665',
        '171886bac78f91b959d78a8679bffb1f94e23b82066f7a15f88e7b24b5ca9739': "The engravings start to violently glow as the inside of the arched shape starts to open up. \
after a few seconds, the glowing stops and in the place of the clowing arch, there is a steep and narrow staircase that leads downwards. \
As you start going down you feel something pulling you forwards that gets stronger and stronger as you decend. \
Suddenly a flash of light engulfs you and you feel as if you where thrown at the speed of light forwards \
and you don't have any way of stopping it. \nIt all goes white."
    }
}

NPCmsgs = {
    
    'NPC': {
        'Aname': [0,0,0,0,[''],True],
        'Cocroach': [0,0,0,0,['Special Torch'],False],
    },
    'Bosses': {
        'Cocroach': [[100,40,80,20,['Coin','Wand']],[-99,-30,-70,0,['Torch', 'Red Potion']]],
    },

    'NPCS': {
        'AAign': "",
    }
}


# List of debug (Tilde) Commands

debugList = ["Where","Chngmsgs","Tp","Pu","Edithealth","Chngname","Additem"]

#Define Iems CLass
class Items:
    def __init__(self, Buffs: list, canBeUsed: bool, SingleUse: bool, msgt: bool, msg: str):
        self.Health = Buffs[0]
        self.Protection = Buffs[1]
        self.Power = Buffs[2]
        self.Magic = Buffs[3]
        self.canBeUsed = canBeUsed
        self.singleUse = SingleUse
        self.msgt = msgt
        self.msg = msg

#Define Item Objects

#Compass messages
with open("story.txt","r") as fi:
    for ln in fi:
        if ln.startswith(f"C- {currentRoom}"):
            compassMsg = ln.partition(': ')[-1]
            break

#Items
Compass = Items([0,0,0,0],True,False,True,compassMsg)
Coin = Items([2,2,0,1],False,False,False,"")
Sand = Items([-10,5,-10,0],False,False,False,"")
BreadLoaf = Items([5,0,2,0],True,True,True,"Your health has increased by 5 and your power has increased by 2")
WhackyPotion = Items([randint(-11,11),randint(-5,5),randint(-5,5),randint(-5,5)],True,True,True,"Random effects are upon you!")
Wand = Items([50,50,90,30],False,False,False,"")
SpecialTorch = Items([0,0,0,0],False,False,False,"")
RedPotion = ([20,0,7,0],True,True,True,"Your health has increased by 20 and your power has increased by 7")