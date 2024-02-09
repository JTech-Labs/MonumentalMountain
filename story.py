from random import randint

currentRoom = "Superliminal Space"

places = {
    'Superliminal Space': {'Forwards': 'Mountain Base', 'Right': 'Forrest Start', 'Left': 'Desert Start', 'Down': 'Tilled Land'},
    'Mountain Base': {'Backwards': 'Superliminal Space', 'Item': 'Whacky Potion'},
    'Forrest Start': {'Backwards': 'Superliminal Space', 'Item': 'Wand'},
    'Desert Start': {'Forwards': 'Desert Canyon', 'Right': 'Desert Shadow', 'Left': 'Desert Rocks', 'Backwards': 'Superliminal Space', 'Item': 'Bread Loaf'},
    'Tilled Land': {'Item': 'Compass'},
    'Desert Shadow': {'Backwards': 'Desert Start', 'Item': 'Coin'},
    'Desert Rocks': {'Secret': [
    "a0ead0b63e9ddc749106e77da630106b5be5d9a5c0be43e96098325f7ba9377d",
    "b743d651ac4a114940c1d141929b9ee08ad3c5cdc38e1d299bd307e4811639ae",
    "171886bac78f91b959d78a8679bffb1f94e23b82066f7a15f88e7b24b5ca9739"], 'Back': 'Desert Start'},
    'Desert Canyon': {'Boss': 'Cocroach', 'Backwards': 'Desert Start', 'Item': 'Sand', 'Forwards': 'Further Desert Canyon'},
    'Further Desert Canyon': {'Backwards': 'Desert Canyon', 'Req': 'Special Torch'}
}

msgs = {
    'Superliminal Space': "You look forwards, at the crossroads, a slightly superliminal place.\
 A path directly ahead of you leads to a giant grey, snow-capped mountain shrouded by clouds\
 which half hides the bright sun. To the right there is a path leading to a green and\
 life-filled forest. The treetops are shrouded by storm clouds and a dark atmosphere\
 emanates from it. The left path leads to a barren and arid desert with a few littered\
 canyons and scorching heat that can be felt even from here.",

    'Forrest Start': "You decide that this is the best option for food and that it will be easier to survive.",

    'Mountain Base': "You are filled with a burning curiosity and decide to make headway for the mountain.",
    
    'Desert Start': "Even though you might not find water there you think it is the best option for refuge. \
You slowly stroll forwards, brushing the sand with your feet as the sun scorches the back of your neck. \
You see a set of large rocks to the left that look like could be good for refuge and might be a bit humid. \
You can also see a small shadow far off to the right and think it could be an oasis. \
Or you could carry on forwards just incase you find anything better.",
    
    'Desert Shadow': "After some walking, you find a palm tree with an \"X\" carved into it, \
as this had always meant treasure in your world, you dig a few centimeters and find a small coin, \
when you go to touch it, a surge of power ruches through you as you feel an increase of energy traveling through you body. Now you can only go backwards.",

    'Desert Rocks': "You find a few boulders grouped seemingly randomly around a larger center boulder \
where a line of text written in the same language as on your cuff bracelet  an ark ",

    'Desert Canyon': "You slowly go down to the canyon to see what's there. As you preceed, \
you see the great expanse of the land, with the yellow sand that expands to the horizon.",

    'Tilled Land': "You decided that you don't want to go in the traditional directions presented to you, \
and you decide to start digging downwards. You appear into a secret network of tunnels underneath the map that no oe knew existed."

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

Items = {
    'Compass': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}, 'SingleUse': False, 'msgt': compassMsgs[currentRoom]['T'], 'msg': compassMsgs[currentRoom]['msg']},
    'Coin': {'Buffs': {'Health': 2, 'Protection': 2, 'Power': 0, 'Magic': 1}},
    'Sand': {'Buffs': {'Health': -10, 'Protection': 5, 'Power': -10, 'Magic': 0}},
    'Bread Loaf': {'Buffs': {'Health': 5, 'Protection': 0, 'Power': 2, 'Magic': 0}, 'SingleUse': True, 'msgt': True, 'msg': 'Your health has increased by 5 and you power has increased by 2'},
    'Whacky Potion': {'Buffs': {'Health': randint(-11,11), 'Protection':  randint(-5,5), 'Power': randint(-5,5), 'Magic': randint(-5,5)}, 'SingleUse': True, 'msgt': True, 'msg': 'Random effects are upon you!'},
    'Wand': {'Buffs': {'Health': 50, 'Protection': 50, 'Power': 90, 'Magic': 30}},
    'Special Torch': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}},
    'Red Potion': {'Buffs': {'Health': 20, 'Protection': 0, 'Power': 7, 'Magic': 0}, 'SingleUse': True, 'msgt': True, 'msg': 'Your health has increased by 20 and you power has increased by 7'},
    'Torch': {'Buffs': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0}},
}
