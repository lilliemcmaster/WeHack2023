# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("[povname]", who_color="#fc4fff")
define j = Character("Jonathon", who_color="#ff5e4f")
define n = Character("Mysterious Voice", who_color="#4f87ff")
define role = "unknown"
define gui.text_font = "kongtext.TTF"
# define gui.text_size = 50

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene clouds
    n "Hello, welcome to the world of Orb Quest. This is an interactive text game."
    n "First we will start with your name. This cannot be changed, try not to pick something too silly."
    python:
        povname = renpy.input("What would you like to be called? ", length=32)
        povname = povname.strip()
        if not povname:
            povname = "mystery"
    n "It's nice to meet you, [povname]"
    n "While sleeping, you dream of a world of magic and mystery. "
    n "In this dream, you play a role of great importance. However, you are having a hard time remembering which role you play."
menu:
    "Physicist":
        $ role = "physicist"
        jump intro
    "Computer Scientist":
        $ role = "computer scientist"
        jump intro
    "Biologist":        
        $ role = "biologist"
        jump intro
    "Chemist":
        $ role = "chemist"
        jump intro 
    # This ends the game.

return

label intro:
    scene cave
    n "As you open your eyes, you vaguely remember you are a [role]."
    j "Oh, you're awake! I'm Jonathon. I'm sorry to have startled you."
    j "I need the help from a [role] and I know you're the best there is."
    u "Where am I?"
    j "You're in my home deep inside the Erudition Forest."
    j "There's an evil scientist who is making Energy Orbs to disturb the balance of our sacred forest."
    j "I need your help to travel through the Forest and stop the scientist."
    scene cave empty
menu: 
    "Yes":
        j "You are so brave! Lets begin our adventure."
        jump railroad
    "No":
        j "Don't be silly, [povname] ! I know you are smart, and this is a challenge of smarts!"
        jump railroad
    j "Will you help me?"
    #end game
return

label railroad:
    scene cave out
    n "You approach the cave exit."
    n "You have the options to use a pulley, a ladder, or hammer."
python:
    flag = 1
while flag == 1:
    menu:
        "Ladder":
            j "Oooohhhh noooo. I've eaten way too many cookies so I won't be able to fit in that tiny crack on the top."
            j "We need to find a way to make more space."
        "Lift it":
            j "Okay let's pick it up on 1 .. 2 ... 3 ..."
            j "eerrggghhhh .... [povname] I don't think we are strong enough to pick it up."
            j "Maybe we need a tool to help with the weight."
        "Pulley System":
            j "Great Idea! We can use a rope and a few wheels to spread out the weight of the boulder."
            j "The weight distrubution allows us to pull it up with less effort!"
            scene cave up
            n "The boulder lifts with the pulley system."
            python:
                flag = 0
        n "How should you open the cave door?"
scene orb
n "You have earned an Orb!"



