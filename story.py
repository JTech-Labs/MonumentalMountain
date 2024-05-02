from random import randint

currentRoom = "Superliminal Space"

places = {
    'Superliminal Space': {'Forwards': 'Mountain Base', 'Right': 'Forrest Start', 'Left': 'Desert Start', 'Down': 'Tilled Land', 'msgs': 3},
    'Mountain Base': {'Backwards': 'Superliminal Space', 'Item': 'Whacky Potion', 'msgs': 7},
    'Forrest Start': {'Backwards': 'Superliminal Space', 'Item': 'Wand', 'msgs': 5},
    'Desert Start': {'Forwards': 'Desert Canyon', 'Right': 'Desert Shadow', 'Left': 'Desert Rocks', 'Backwards': 'Superliminal Space', 'Item': ['Bread Loaf']},
    'Tilled Land': {'Item': 'Compass'},
    'Desert Shadow': {'Backwards': 'Desert Start', 'Item': ['Coin']},
    'Desert Rocks': {'Secret': [
    "a0ead0b63e9ddc749106e77da630106b5be5d9a5c0be43e96098325f7ba9377d",
    "b743d651ac4a114940c1d141929b9ee08ad3c5cdc38e1d299bd307e4811639ae",
    "171886bac78f91b959d78a8679bffb1f94e23b82066f7a15f88e7b24b5ca9739"], 'Back': 'Desert Start'},
    'Desert Canyon': {'Boss': 'Cocroach', 'Backwards': 'Desert Start', 'Item': 'Sand', 'Forwards': 'Further Desert Canyon'},
    'Further Desert Canyon': {'Backwards': 'Desert Canyon', 'Req': 'Special Torch'}
}

secMsgs = {
    'Desert Rocks': {
        'ae': 'Welcome J-A-I',
        '39': u'\u2665',
        '7d': "The engravings start to violently glow as the inside of the arched shape starts to open up. \
after a few seconds, the glowing stops and in the place of the clowing arch, there is a steep and narrow staircase that leads downwards. \
As you start going down you feel something pulling you forwards that gets stronger and stronger as you decend. \
Suddenly a flash of light engulfs you and you feel as if you where thrown at the speed of light forwards \
and you don't have any way of stopping it. \nIt all goes white."
    }
}

compassMsgs = {
    'Superliminal Space': {'msg': "This is a superliminal place.\n\
Superliminal is a term used in psychology and physiology to describe mental activity that is above the threshold of the subconscious. \
It is the opposite of subliminal, which refers to mental activity that is below the threshold of conscious awareness. \
The term supraliminal is also used to describe mental activity that is above the threshold of consciousness.", 'T': True},
    'Desert Start': {'T': False},
    'Tilled land': {'T': False}
}

NPCmsgs = {
    
    'NPC': {
        'Aname': {'Conv': 'Hello, I am a Non-Playable Character!'},
        'Cocroach': {'Conv': "Even though you find this unknown animal very frightening, you decide to gently hush in order to calm it down. \
The cockroach looks at you with confusion. To your surprise it responds and says 'What are you doing? I am the guardian of the Isoriac dessert. \
My unlucky body normally frightens most people but I'm actually very friendly! You discover that its name in Inorilarn, \
the long forgoten language of this land, and that it has been here since the first ray of light dried the sandy place. \
He hasn't talked to anyone in a lot of time as most adventurers are too terrified.", 'PU': [0,0,0,0,'Special Torch']},
    },
    'Bosses': {
        'Cocroach': {'FightLose': "You fight until you don't have any more energy even though the beast doesn't make a single move. \
The cockroach looks at you with sorrow and disappointment. You find a hill up which you can go back..", 'Req': [100,40,80,20,['Coin','Wand']],
'FightWin': "You win!", 'Effects': {'Health': -99, 'Protection': -30, 'Power': -70, 'Magic': 0, 'Item': ['Torch', 'Red Potion']}},
    },

    'NPCS': {
        'Asign': {'Tex': 'Hello, I am a signpost!'},
    }
}


#Define Iems CLass
class Items:
    def __init__(self, Buffs: list, canBeUsed: bool, SingleUse: bool, msgt: bool, msg: str):
        self.Protection = Buffs[1]
        self.Power = Buffs[2]
        self.Magic = Buffs[3]
        self.canBeUsed = canBeUsed
        self.singleUse = SingleUse
        self.msgt = msgt
        self.msg = msg

#Define Item Objects
Compass = Items([0,0,0,0],True,False,True, with open("story.txt","r") as fi: for ln in fi: if ln.startswith(f"C- {currentRoom}"): printSlow(ln.partition(': ')[-1]); break)
Coin = Items([2,2,0,1],False,False,False,"")
Sand = Items([-10,5,-10,0],False,False,False,"")
BreadLoaf = Items([5,0,2,0],True,True,True,"Your health has increased by 5 and your power has increased by 2")
WhackyPotion = Items([randint(-11,11),randint(-5,5),randint(-5,5),randint(-5,5)],True,True,True,"Random effects are upon you!")
Wand = Items([50,50,90,30],False,False,False,"")
SpecialTorch = Items([0,0,0,0],False,False,False,"")
RedPotion = ([20,0,7,0],True,True,True,"Your health has increased by 20 and your opwer has increased by 7")

##Items = {
#    'Compass': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}, 'SingleUse': False, 'msgt': compassMsgs[currentRoom]['T'], 'msg': compassMsgs[currentRoom]['msg']},
#    'Coin': {'Buffs': {'Health': 2, 'Protection': 2, 'Power': 0, 'Magic': 1}},
#    'Sand': {'Buffs': {'Health': -10, 'Protection': 5, 'Power': -10, 'Magic': 0}},
#    'Bread Loaf': {'Buffs': {'Health': 5, 'Protection': 0, 'Power': 2, 'Magic': 0}, 'SingleUse': True, 'msgt': True, 'msg': 'Your health has increased by 5 and you power has increased by 2'},
#    'Whacky Potion': {'Buffs': {'Health': randint(-11,11), 'Protection':  randint(-5,5), 'Power': randint(-5,5), 'Magic': randint(-5,5)}, 'SingleUse': True, 'msgt': True, 'msg': 'Random effects are upon you!'},
#    'Wand': {'Buffs': {'Health': 50, 'Protection': 50, 'Power': 90, 'Magic': 30}},
#    'Special Torch': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}},
#    'Red Potion': {'Buffs': {'Health': 20, 'Protection': 0, 'Power': 7, 'Magic': 0}, 'SingleUse': True, 'msgt': True, 'msg': 'Your health has increased by 20 and you power has increased by 7'},
#    'Torch': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}},
#}

