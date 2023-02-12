# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("[povname]")
define j = Character("Jonathon")
define n = Character("Mysterious Voice")
define role = "unknown"

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
    n "As you open your eyes, you vaugly remember you are a [role]."
    j "Oh, you're awake! I'm Jonathon. I'm sorry to have startled you."
    j "I need the help from a [role] and I know you're the best there is."
    u "Where am I?"
    j "You're in my home deep inside the Erudition Forrest."
    j "There's an evil scientist who is making Energy Orbs to disturb the balance of our sacred forrest."
    j "I need your help to travel through the Forrest and stop the scientist."

menu: 
    "Yes":
        j "You are so brave! Lets begin our adventure. First, we have to open the cave door."
        jump cavedoor
    "No":
        j "Don't be silly, [povname] ! I know you are smart, and this is a challenge of smarts!"
        jump cavedoor
    j "Will you help me?"
    #end game
return

