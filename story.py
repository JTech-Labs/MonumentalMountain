places = {
    'Superliminal Space': {'Forewards': 'Mountain Base', 'Right': 'Forrest', 'Left': 'Desert Start', 'Item': 'Coin'},
    'Mountain Bade': {'Item': 'Compass'},
    'Desert Start': {'Forewards': 'Desert Canyon', 'Right': 'Desert Shadow', 'Left': 'Desert Rocks', 'Back': 'Superliminal Space'},
    'Desert Shadow': {'Back': 'Desert Start', 'PU': {'Health': 100, 'Protection': 100, 'Power': 100, 'Magic': 100}},
    'Desert Rocks': {'Secret': ["a0ead0b63e9ddc749106e77da630106b5be5d9a5c0be43e96098325f7ba9377d",
"b743d651ac4a114940c1d141929b9ee08ad3c5cdc38e1d299bd307e4811639ae"], 'Back': 'Desert Start'},
    'Desert Canyon': {'Boss': 'Cocroach', 'Back': 'Desert Start', 'Item': 'Sand'},
}

msgs = {
    'Superliminal Space': "You look forwards, at the crossroads, a slightly superliminal place.\
 A path directly ahead of you leads to a giant grey, snow-capped mountain shrouded by clouds\
 which half hides the bright sun. To the right there is a path leading to a green and\
 life-filled forest. The treetops are shrouded by storm clouds and a dark atmosphere\
 emanates from it. The left path leads to a barren and arid desert with a few littered\
 canyons and scorching heat that can be felt even from here.",
    
    'Desert Start': "Even though you might not find water there you think it is the best option for refuge. \
You slowly stroll forwards, brushing the sand with your feet as the sun scorches the back of your neck. \
You see a set of large rocks to the left that look like could be good for refuge and might be a bit humid. \
You can also see a small shadow far off to the right and think it could be an oasis. \
Or you could carry on forwards just incase you find anything better.",
    
    'Desert Shadow': "After some walking, you find a palm tree with an \"X\" carved into it, \
as this had always meant treasure in your world, you dig a few centimeters and find a small coin, \
when you go to touch it, a surge of power ruches through you as you feel an increase of energy traveling through you body. \
You blink for a second and the coin disappears. Now you can only go back.",

    'Desert Rocks': "You find a few boulders grouped seemingly randomly around a larger center boulder \
where a line of text written in the same language as on your cuff bracelet  an ark "

}

secMsgs = {
    'Desert Rocks': {'ae': 'Welcome Javi!', '7d': "The engravings start to violently glow as the inside of the arched shape starts to open up. \
after a few seconds, the glowing stops and in the place of the clowing arch, there is a steep and narrow staircase that leads downwards. \
As you start going down you feel something pulling you forewards that gets stronger and stronger as you decend. \
Suddenly a flash of light engulfs you and you feel as if you where thrown at the speed of light forwards \
and you don't have any way of stopping it. \nIt all goes white."}
}

compassMsgs = {
    'Superliminal Space': 'This is a superliminal place.\n\
Superliminal is a term used in psychology and physiology to describe mental activity that is above the threshold of the subconscious. \
It is the opposite of subliminal, which refers to mental activity that is below the threshold of conscious awareness. \
The term supraliminal is also used to describe mental activity that is above the threshold of consciousness.',
    'Desert Start': '',
}

NPCmsgs = {
    
    'NPC': {
        'Aname': {'Conv': 'Hello, I am a Non-Playable Character!'},
        'Cocroach': {'Conv': "Even though you find this unknown animal very frightening, you decided to gently hush in order to calm it down. \
The cockroach looks at you with confusion. To your surprise it responds and says 'What are you doing? I am the guardian of the Isoriac dessert. \
My unlucky body normally frightens most people but I'm actually very friendly! You discover that its name in Inorilarn, \
the long forgoten language of this land, and that it has been here since the first ray of light dried the sandy place. \
He hasn't talked to anyone in a lot of time as most adventurers are too terrified.", 'PU': []},
    },
    'Bosses': {
        'Cocroach': {'FightLose': "You fight until you don't have any more energy even though the beast doesn't make a single move. \
The cockroach looks at you with sorrow and disappointment. You find a hill up which you can go back..", 'Req': [200,100,100,100,"Coin"],
'FightWin': "You win!", 'Effects': {'Health': -100, 'Protection': -20, 'Power': -10, 'Magic': 0}},
    },

    'NPCS': {
        'Asign': {'Tex': 'Hello, I am a signpost!'},
    }
}

Items = {
    'Compass': {'Health': 0, 'Protection': 0, 'Power': 0, 'Magic': 0},
    'Coin': {'Health': -5, 'Protection': 5, 'Power': -5, 'Magic': 0}
}