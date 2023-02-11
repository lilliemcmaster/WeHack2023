import random
import time #used this for life system (i think)

nameresp =["Nice, it's actually a decent name", "That's an interesting name....",
            "I said to try not to pick something stupid, but fine, let's go with this I guess",
            "That's better than most I suppose", "A good name", "That's a name I suppose...",
            "Why would you choose that...?"]
hp = 15 #var for hp
incorrect_count = 0
escape1 = 0

#define function for incorrect entries
def incorrectentry (incorrect_count):
    hp = hp - 1
    incorrect_count = incorrect_count+1
    print ("That was not an option. I will assume it's a typo. Try to to do that again.\n")
    print("You have lost 1 HP. You now have " + hp + " left.\n")

def section1 (hp, escape1):
    print("So, what would you like to do first? You can 'look around', 'stay put', or 'search for keys'\n")
    userin = input("Enter your choice here:")
    if (userin == "look around" or " look around "):
        print("Good on you for trying to be observant. But alas, you're blind folded.")
        print("You wait for a moment, and hear footsteps. They are load and thud a little. You assume it means the person is big.")
        print("They grab you by the collar and take off your blind fold")
        print("As your sight returns, you notice this person is not big, they are simply covered in armor. The kind you could flick and it would fall off.")
        print("As your eyes focus on their face, you see that this person is you friend from the cell next to you.")
        print("What do you do now? You can 'talk to them', 'look around', 'say something goofy'")
        userin = input("Enter your choice here: ")
        if (userin == 'say something goofy'):
            print("You talk to your friend. They are very happy to see you.\n")
            print("'I didn't think I'd make it out of that cell "+username+ "' They said. 'I'm glad I got out and managed to get you out as well.'\n")
            print("You nod in agreement. But just as you are about to say something more, a large belch escapes from your mouth, alerting a nearby guard.\n")
            print("He runs up to you and unsheaths his sword. 'Prisoners who atempt to escape, by royal decree, are to consider their lives forfeit!'.\n")
            print("With a mighty bellow, he cuts off your head.")
            hp = 0
        elif (userin == 'look around'):
            print("Being observant is usually a very good trait. In this case it saved your life.")
            print("You notice a guard is coming down the hallway. In this kingdom, atempting to escape will likely lead to your death.")
            print("Needless to say, it is best to avoid getting caught.")
            print("You gesture to the guard, and your friend quickly drops you. You land with a thud that you're sure will bruise.")
            print("They give you a confused look, as they have the same number of braincells as a door mat.")
            print("What do you do now? You can tell your friend to 'act like guard', 'go back to cell', or 'stay put'")
            userin = input("Enter your choice here: ")
            if (userin == "act like guard"):
                print("Smart move. Your friend rushed out the door and stand in some form of attention.")
                print("Unfortunately for you, the guard that walks by is the chief inspector, and notices that your friend is not a guard.")
                print("He also notices that your cell is open.")
                print("He runs up to you and unsheaths his sword. 'Prisoners who atempt to escape, by royal decree, are to consider their lives forfeit!'.\n")
                print("With a mighty bellow, he cuts off your head.")
                hp = 0
                escape1 = 0
            elif (userin == "go back to cell"):
                print("Smartest move. Your friend rushed out the door to stand in his cell.")
                print("Unbeknownst to you, the guard that walks by is the chief inspector, and would have noticed your friend was not a guard.\n")
                print("He walks in to speak with you, impressed by your ability to resist the temptation to run out.\n")
                print("He runs up to you and unsheaths his sword. 'Prisoners who atempt to escape, by royal decree, are to consider their lives forfeit!'.\n")
                print("However, your commitment to remain has impressed me greatly. I will seek to grant you audience with the king\n")
                print("Congratulations, you have escaped the dungeon!")
                escape1 = 1
                return(escape1)
    elif (userin == "stay put"):
        print("You stay put, but as a result, your friend in the cell next to you believes you to be dead.\n")
        print("Without their interferance, you remain in the cell, rotting away, and eventually die :) \n")
        hp = 0
        escape1 = 0
    elif (userin == "search for keys"):
        print("As you shuffle around looking for keys, you don't notice a guard coming towards you. However, he does notice your attmepted escape.\n")
        print("He runs up to you and unsheaths his sword. 'Prisoners who atempt to escape, by royal decree, are to consider their lives forfeit!'.\n")
        print("With a mighty bellow, he cuts off your head.")
        hp = 0
        escape1 = 0
    return(escape1)  

#introduction
I1 = "Hello User, welcom to the world of Laetus \n"
I2 = "This is an interactive text game. To proceed with the game, enter one of the options provided."
I3 = "Please remember to enter the exact options shown in the prompt, down to the letters and spaces - \n otherwise the world might kill you.\n"
I4 = "First we will start with your name. This cannot be changed, try not to pick something too stupid.\n"
print(I1+"\n"+I2+"\n"+I3+"\n"+I4+"\n")

#welcome user to the game
username = input("What would you like to be called? ")
print(random.choice(nameresp)+"\n")
print("Welcome " + username + ". \n")

while (hp > 0): #start the game, run while hp > 0
    escape1 = 0
    print("Through some unforseen circumstances you find yourself stuck in a castle dungeon.\n")
    print ("It is damp and cold and altogether miserable.\n")
    print("This is where the game starts.\n")
    section1(hp, escape1)
    if (escape1 == 1):
        print ("Congrats on completing the game so far!")
        sys.exit()
print("You have died, good luck trying again!")
