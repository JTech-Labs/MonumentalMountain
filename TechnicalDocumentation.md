# The Technical Docuementation for the _**Perspectiva Engine**_ used by MonumentalMountain

This docuementation is split into two main categories: the _code comments_ and [_this file_](TechnicalDocumentation.md).
The function and workings of ~~every~~ most part of the code will be explained here, along with the purpose and design of the _JSON game files_.

## The JSON file 

This is what actually constitutes the game itself, the code is really just the engine which interprets this file and presents the story to you.
In this section the workings and meanings of the different parts of the JSON file will be detailed as a reference.

## The `_` section

This section defines all the debuging and explanitory parts of the file.
It contains these keys:

 - [_LANG_]: Used to confirm the language loaded is the one requested
 - [_NAME_]: Used for the print message of what language has been loaded

## The `STORY` section

This contains the grand majority of the data in a JSON file and where everything else is defined

### `map`

This contains what is essentially the map of the land, it is a bit hard to read as it is a one-dimensional listing of all the places without easily identifiable
connections between them, but oh well, I'll come up with something beter in the future, probably, maybe...

Structure:

 - "<Name of location>": {
    - "Forwards": "<Place you go when you go forwards>",

      This is then repeated for all the other available directions, of which you can choose any and however you want.
      Available directions: `Forwards`, `Backwards`/`Back`, `Left`, `Right`, `Upwards`/`Up`, `Downwards`/`Down`

    - "Item": ["<A list of the items found there"]

    - (Optional)
      
      "Req": ["<A list of the items required to enter a place"]

### `story` (lowercase this time)

This is where the big chunk happens, it is the description of each of the places which can be visited.
The structure is very simple:

"<Name of place>": "<Message to be printed>"

### `compass`

These are the further detailed messages for each place given by the compass.
It has the same structure as that of the [previous section](###-`story`-(lowercase-this-time))


### Interactions

There are three different type of interactions with objects in the environment: `talk`/`speak`/`speakwith`, `read`, and `fight`

The structure for `talking`:

 - "<Name>": [
    - "<Here you put whatever you want your thing to say>",
    - "<You can put as many different phrases as you want (there are no dialog __options__ yet, #TODO: work on this in the future!)>",
    - "<The last phrase you put works in a special way, it is the message given for when your thing isn't there anyomre"
 - ]

Fighting works in the same way, except that the last two phrases work like this (in order):

 - The penultimate phrase works for when someone comes back after being defeated, then one of the normal ones gets printed underneath
 - The last phrase works for when someone comes back to fight an enemy they have already defeated, then exits the fight.
    - TODO: make a better fighting system
    - TODO: more interactive enemies

For `reading` you just write `"<Name>": "<The text to read>"`

