# Program Name: Bark.py
# Developer: Zar Qureshi
# Date: 03/02/2018
# Description: Project 1. A game about a child that has a neighbor named Steve, who has a dog named Bark.
#              Steve doesn't like Bark, because he was always ruining the furniture, barking non-stop, and was far too aggressive.
#              The neighbor bought a cheap dog house that he placed in his front yard. He hammered down a nail where Bark's leash came out of.
#              As a result, Bark is always outside, and you pass by him everytime you're walking to and from school. You will play for a
#              certain amount of days, and will have actions to pick from each of those days. The actions you pick will shape the outcome of the game.

import time as t

# Displays the introduction line of the game
def displayIntro(name):
    print("Hello, " + name + """. Welcome to Bark! This is a story about you and your neighbor's dog!
You will have a certain amount of days to go to school,
and you'll interact with the dog each time with options given.\n""")
    t.sleep(2)
    print("Press enter to start playing! Everytime you see \">\", you'll be required to press enter to continue. >")
    input()
    
# Dialogue function, includes the name of the person talking, then waits until user enters to continue
def sendDialogue(name, message):
    print("["+name+"]" + ":", message, ">")
    input()
    
# Sends the user the summary of one of the days.
def sendDaySummary(sumlist, action):
    print("\nHere's what has happened so far:")
    sumlist.sort()
    for dc in sumlist:
        print(dc)
    condition = ""
    if (action["Relationship"] < 0):
        condition = "Bad"
    elif (action["Relationship"] == 0):
        condition = "Moderate"
    elif (action["Relationship"] > 0):
        condition = "Good"
    print("Current Relationship with Bark:", str(action["Relationship"]), "(" + condition + ")")
    input(">")

# Sends options selection
def sendOptions(a, b, c, d = ""):
    response = ""
    if (d != ""):
        print("What will you do? Make a selection:\n\t A)", a, "\n\t B)", b, "\n\t C)", c, "\n\t D)", d)
        while (response != "A" and response != "B" and response != "C" and response != "D"):
            response = input().upper()
    else:
        print("What will you do? Make a selection:\n\t A)", a, "\n\t B)", b, "\n\t C)", c)
        while (response != "A" and response != "B" and response != "C"):
            response = input().upper()
    return response

# Runs each day with a day number and action dict parameter
def startDay(name, day, action):
    choice = ""
    print("------------Day", day,"------------")
    t.sleep(1.5)
    if (day == 1):
        print("It's a nice and sunny day. The birds are chirping outside your window.")
        t.sleep(2)
        print("Everything's great. You're asleep still, dreaming about playing your favorite video game. Your alarm starts ringing.")
        t.sleep(2)
        print("7:00 AM")
        for i in range(3):
            print("BEEP!")
            t.sleep(0.5)
        print("You come out of your great sleep, and slam the alarm shut.")
        sendDialogue(name, "I don't want to go... maybe I'll sleep a little longer.")
        sendDialogue(name, "*Actually, I think I can miss a day of school. Four days out of five is good enough, right?*")
        print("You shut your eyes once more, and the next thing you know, you're dreaming again.")
        sendDialogue("Mom", "Hey! " + name + "! Why are you still sleeping? You can't keep missing school.")
        sendDialogue("Mom", "You end up skipping every Wednesday. You'll end up failing if you miss a day of school literally once every week.")
        sendDialogue("Mom", "If you don't get up right now, I'll take off your blanket and open up the window. NOW "+ name+ ", I mean it.")
        sendDialogue(name, "Alright, alright, I'm getting up. It's only been five minutes since my alarm rang, it's no big deal. I wasn't planning on skipping.")
        sendDialogue("Mom", "I'm sure you weren't. I'll warm up some waffles for you. Just hurry up and get dressed.")
        print("You get ready for school and go downstairs to the kitchen.")
        sendDialogue("Mom", "Remember. Straight to school and back.")  
        sendDialogue(name, "I know mom. Don't worry.")
        print("You finish eating and pick up your backpack.")
        t.sleep(0.6)
        print("You walk out the front door and head to the sidewalk.")
        t.sleep(0.6)
        print("A couple steps forward, you reach your neighbor, Steve's house.")
        t.sleep(1)
        print("You see his dog, a black rottweiler named Bark.")
        t.sleep(1)
        sendDialogue(name, "Well, there's Bark. He always rushes towards me when I walk past him.")
        sendDialogue(name, "One day he's going to break out of his leash and make me his meal.")
        sendDialogue(name, "I really wish Steve didn't leave him out like this, all the time. The whole neighborhood's tired of Bark's barking at this point.")
        print("You begin to walk alongside Steve's front yard...")
        t.sleep(2)
        print("Bark's dog-house comes in your sight, where Bark could be seen chasing after his own tail.")
        t.sleep(2)
        print("You continue to walk.")
        sendDialogue(name, "Wow, he hasn't run after me yet-")
        print("As soon as you say that, Bark charges at you, hitting the fence with force.")
        t.sleep(1)
        sendDialogue("Bark", "BARK! BARK! BARK!")
        print("You jump back from the fence, letting out a little scream.")
        t.sleep(1.3)
        choice = sendOptions("Kick the fence Bark is leaning on", "Scold Bark", "Do nothing and proceed to school", "Be friendly to Bark")
        if (choice == "A"):
            action["Relationship"] -= 2
            action["LatestChoice"] = ("Day 1", "Kicked the fence Bark was leaning on.")
            print("You bring your leg back, and charge a strong kick onto the fence, where Bark was leaning.")
            t.sleep(1.5)
            sendDialogue("Bark", "*Snaps back, stops barking*")
            sendDialogue(name, "That should teach you not to jump at me!")
            sendDialogue("Bark", "*Growls*")
            sendDialogue(name, "Yeah, yeah, whatever.")
            t.sleep(1)
        elif (choice == "B"):
            action["Relationship"] -= 1
            action["LatestChoice"] = ("Day 1", "Scolded Bark for startling you.")
            sendDialogue(name, "Bark! Stop it! Off the fence! Don't scare me like that!")
            sendDialogue(name, "Bad dog!")
            sendDialogue("Bark", "*Whine*")
            sendDialogue(name, "Don't whine at me... you had it coming.")
        elif (choice == "C"):
            action["LatestChoice"] = ("Day 1", "Bark jumped at you from his leash, but you decided not to react.")
            print("You decide not to interact with Bark.")
            t.sleep(2)
            print("As you continue walking, Bark keeps at you like a magnet on the opposite side of the fence.")
            t.sleep(2.5)
            print("Then his leash reached it's limit, and he was knocked down by it.")
            sendDialogue("Bark", "BARK! BARK BARK! *growl*")
            sendDialogue("Bark", "...")
            print("Bark keeps his eyes on you as you walk away.")
            t.sleep(2)
        elif (choice == "D"):
            action["Relationship"] += 2
            action["LatestChoice"] = ("Day 1", "You put your hand out near Bark's mouth, and he licked it.")
            print("You get closer to the fence.")
            t.sleep(2)
            sendDialogue(name, "I hope I don't regret this...")
            sendDialogue(name, "Don't worry, Bark. Calm down, doggo.")
            sendDialogue("Bark", "*Stops barking, and begins to sniff at your nose.*")
            sendDialogue("Bark", "*After sniffing for a while, he takes out his tongue and starts licking your fingers.*")
            sendDialogue(name, "Haha! That tickles.")
            sendDialogue(name, "Maybe you're not as bad as I thought.")
            sendDialogue(name,"Well, I should head off to school. I'll see you later, Bark.")
            print("As you're walking away, Bark continues his barking.")
            t.sleep(2)
        print("You proceed to go to school.")
        t.sleep(1)
    elif (day == 2):
        print("7:00 AM")
        for i in range(3):
            print("BEEP!")
            t.sleep(0.5)
        sendDialogue(name, "*Shuts off alarm*")
        sendDialogue(name, "Another day, another dollar.")
        sendDialogue(name, "Oh wait, I don't make money.")
        print("Your mother walks into your room.")
        t.sleep(2)
        sendDialogue("Mom", "Good! You're awake. Keep it up " + name + "!")
        sendDialogue(name, "Quite easy, mom.")
        print("You do your daily wake up routine and head outside.")
        t.sleep(2)
        if (action["Relationship"] < 0):
            print("Once you saw Bark, he locked his eyes on you and began growling.")
            sendDialogue("Bark", "*Growling turns into barking, while attempting to lunge at you with the leash and fence at your defense.*")
        elif (action["Relationship"] == 0):
            print("You saw Bark, in his yard again. He spots you and charges to the fence.")
            sendDialogue("Bark", "BARK! BARK!")
        elif (action["Relationship"] > 0):
            print("Once Bark spotted you, he stopped his restless tail chase and walked towards you.")
            sendDialogue("Bark", "Bark! *Tongue is out, seemingly pleased to see you.*")
            sendDialogue(name, "Hey Bark, how're you doing, boy?")
        sendDialogue(name, "Huh? What happened to your paw?")
        print("You notice Bark has a sharp rock stuck on top of his front left paw. There's a bit of blood dried by it.")
        t.sleep(2.2)
        sendDialogue(name, "That looks like it hurts.")
        choice = sendOptions("Open the gate and help", "Check if Steve is home to help", "Do nothing and proceed to school")
        if (choice == "A"):
            action["Relationship"] += 2
            action["LatestChoice"] = ("Day 2", "You took the risk of getting near Bark to help take out the rock from his paw.")
            sendDialogue(name, "Dont worry Bark, I'll help you get that out.")
            sendDialogue(name, "*You walk to the gate and pull up the lever. You're now in Steve's front yard*")
            sendDialogue("Bark", "*Not used to anyone being in his front yard, Bark continued barking.*")
            sendDialogue(name, "Shh, it's okay, I'm not trying to hurt you.")
            sendDialogue("Bark", "*Bark calmed down*")
            sendDialogue(name, "*You come near Bark and kneel down by his left paw.* This is going to hurt, don't go all rabid on me, please...")
            sendDialogue("Bark", "*Whines*")
            print("Bark jumps back in pain once you took the rock out.")
            t.sleep(2)
            print("He runs to you.")
            t.sleep(1.5)
            print("And licks your shoes playfully.")
            sendDialogue(name, "Good boy! I'm going to head off to school now, thanks for not attacking me. You're really not as bad as I thought.")
        elif (choice == "B"):
            action["Relationship"] -= 1
            action["LatestChoice"] = ("Day 2", "You tried to get Steve to help Bark get the rock out from his paw, but he disregarded it and told you to go to school.")
            sendDialogue(name, "Dont worry, I'll get you some help.")
            sendDialogue(name, "*You walk to the gate and pull up the lever. You're now in Steve's front yard*")
            sendDialogue("Bark", "*Not used to anyone being in his front yard, Bark continued barking.*")
            sendDialogue("Bark", "*He attempts to come to you, but his leash doesn't reach the pathway to the house.*")
            sendDialogue(name, "*You walk up to Steve's door.*")
            print("*Bell rings*")
            t.sleep(4)
            sendDialogue(name, "Guess I'll try again?")
            t.sleep(2)
            sendDialogue(name, "Eh, not home probably?")
            t.sleep(2.1)
            print("*The door opens*")
            sendDialogue("Steve", "Oh, hello. You're my neighbor right? "+ name +"?")
            sendDialogue(name, "Hi, yes I'm " + name + ", your neighbor.")
            sendDialogue(name, "I was just walking to school and I noticed your dog has a rock stuck in his left paw.")
            sendDialogue("Steve", "He does? Oh.")
            sendDialogue(name, "Yes.")
            sendDialogue(name, "He's bleeding from there.")
            sendDialogue("Steve", "Is that right...")
            sendDialogue(name, "Will you take it out for him, please? I'd do it, but I'm worried he'll do something to me if I get that close to him.")
            sendDialogue("Steve", "Tell you what, " + name + ". Don't worry about it.")
            sendDialogue("Steve", "Why don't you head on to school? You must be getting late over this aren't you?")
            sendDialogue(name, "Yes, I just figured it's important to tell you about your dog.")
            sendDialogue("Steve", "Stop stressing about him. I know no one likes him anyway.")
            sendDialogue(name, "He's still a dog. He should be cared for.")
            sendDialogue("Steve", "Kid, just go to school. Really, you don't need to overthink this.")
            sendDialogue(name, "Yes, sir.")
            print("You figured you'd stop trying, he's stubborn about it.")
            t.sleep(1)
        elif (choice == "C"):
            action["Relationship"] -= 3
            action["LatestChoice"] = ("Day 2", "Bark's left paw had a rock stuck in it, he was bleeding, but you decided to not get involved and go to school.")
            sendDialogue("Bark", "*Bark looks at you, he's stopped his barking.*")
            sendDialogue(name, "*You walk away from him.*")
            sendDialogue("Bark", "BARK! *whine* BARK BARK!")
            sendDialogue(name, "*You don't stop walking.*")
        print("You proceed to go to school.")
        t.sleep(1)
    elif (day == 3):
        print("7:00 AM")
        for i in range(3):
            print("BEEP!")
            t.sleep(0.5)
        sendDialogue(name, "*Smacks alarm shut*")
        sendDialogue(name, "Yay! It's Friday!")
        sendDialogue(name, "Took long enough.")
        print("*You're feeling quite energetic today.*")
        t.sleep(1.8)
        sendDialogue(name, "Bye mom!")
        sendDialogue("Mom", "Bye. Remember, I can't pick you up from school today. So, walk home.")
        sendDialogue(name, "Fine by me.")
        print("REMINDER: Your relationship with Bark is at " + str(action["Relationship"]) + ".")
        print("You come out your house, and start your walk to school.")
        t.sleep(2)
        if (action["Relationship"] < 0):
            sendDialogue("Bark", "BARK BARK BARK! *growl*")
            sendDialogue(name, "Ah yes, the wonderful dog named Bark.")
            sendDialogue("Bark", "*Attacking the fence, trying to get to you.*")
            sendDialogue(name, "You're quite the crazy dog. I wonder why Steve hasn't done something more than kick you out of the house.")
            sendDialogue("Bark", "*Continues to growl while trying to attack you.*")
            sendDialogue(name, "Enjoy whatever you're trying to do. I'm going to school.")
        elif (action["Relationship"] == 0):
            sendDialogue("Bark", "BARK! BARK BARK!")
            sendDialogue(name, "*No longer phased from Bark, you continue your walk to school.")
        elif (action["Relationship"] > 0):
            sendDialogue("Bark", "Yip! *Tongue out, standing by the fence*")
            sendDialogue(name, "Hey buddy! How you doing today? ")
            sendDialogue(name, "I was thinking we could play catch after I come home from school. What do you think, boy?")
            sendDialogue("Bark", "*Still joyful, and peaceful. More content than he's been in a really long time.*")
            sendDialogue(name, "Alright, I'll see you soon!")
        print("3:15PM")
        t.sleep(3)
        print("You're walking back home. You reach Steve's house.")
        t.sleep(2)
        if (action["Relationship"] < 0):
            sendDialogue("Bark", "*Growling, looking extremely aggressive, lunging at the fence still, trying to reach you.*")
            sendDialogue(name, "You're really still at it? Jeez.")
            sendDialogue(name, "*You decide to open the gate to start taunting him.*")
            sendDialogue(name, "You want to get me so badly? Come and try, silly dog.")
            sendDialogue("Bark", "BARK BARK BARK BARK")
            print("With one final tug...")
            t.sleep(3.5)
            print("Bark rips the bearing on the ground that held his leash.")
            t.sleep(3.5)
            print("He tackles you.")
            t.sleep(0.5)
            print("*GROWL*")
            t.sleep(0.4)
            print("*BITE*")
            t.sleep(0.5)
            sendDialogue(name, "AHHHH! GET OFF OF ME!")
            print("A neighbor spots you as they were walking down the street, and pulls Bark off you.")
            sendDialogue("Neighbor", "Oh my god, are okay?")
            sendDialogue(name, "My arm! It's bleeding!")
            sendDialogue("Neighbor", "I'm calling 911. You'll be okay; just hang on.")
            print("7:00PM")
            t.sleep(3)
            print("You're in the hospital, with a cast on your arm.")
            sendDialogue("Mom", "*Walks into your room* Feeling any better yet?")
            sendDialogue(name, "Yeah, the painkillers are helping.")
            sendDialogue("Mom", "Okay. I just wanted you to know, you don't have to worry about that dog anymore.")
            sendDialogue(name, "Is Steve FINALLY getting rid of him?")
            sendDialogue("Mom", "Well, since Bark bit you, he's going to be put down.")
            sendDialogue(name, "They're killing him?")
            sendDialogue("Mom", "That's right, "+ name + ".")
            sendDialogue(name, "Oh. I don't know how to feel about that.")
            sendDialogue("Mom", "Try not to think about it so much. What's done is done. I'm sorry that happened to you.")
            sendDialogue(name, "Me too.")
        elif (action["Relationship"] == 0):
            sendDialogue("Bark", "BARK! BARK BARK")
            sendDialogue(name, "You're just trying to grab someone's attention, aren't you?")
            sendDialogue(name, "I hope you know it isn't working, everyone, literally everyone thinks you're annoying.")
            sendDialogue(name, "But, you're still just a dog. Steve shouldn't be neglecting you like this.")
            sendDialogue("Bark", "*Whines, walks back into his dog house.*")
        elif (action["Relationship"] > 0):
            sendDialogue("Bark", "Bark! *Leans to fence's gate*")
            sendDialogue(name, "Hey Bark! *You open the gate* Look what I have?")
            sendDialogue(name, "*You take out a tennis ball from your bag*")
            sendDialogue("Bark", "*Bark comes up to you to grab the ball*")
            sendDialogue(name, "Catch! *You throw the ball by his dog house*")
            sendDialogue("Bark", "*Runs to the ball, and brings it back to you*")
            sendDialogue(name, "Good boy! Let's keep playing!")
    return action


def main():
    playAgain = "Y"
    while playAgain == "Y":
        name = ""
        day = 0
        ans = "Y"
        actiond = {"Relationship" : 0, "LatestChoice" : ""}
        daysummary = []
        while (name == ""):
            name = input("Please enter your name: ")
        displayIntro(name)
        while ((ans == "Y" or ans == "S") and day < 3):
            if (ans == "Y"):
                ans = ""
                day = day + 1
                actiond = startDay(name, day, actiond)
                daysummary.append(actiond["LatestChoice"])
                if (day == 3):
                    ans = "Y"
            elif (ans == "S"):
                ans = ""
                sendDaySummary(daysummary, actiond)
            while (ans != "Y" and ans != "S"):
                print("Would you like to continue to the next day? Your options are:\n Y) Continue to next day \n S) View a summary of what's happened so far.")
                ans = input().upper()
        print("The end! Summary:")
        sendDaySummary(daysummary,actiond)
        playAgain = input("Play again? Y) Yes N) No   :").upper()        
main()
