import os #for linesep
import sys
from subprocess import * #for linux commandline utility
from random import * #randint funciton

class Introduction():

    def __init__(self):

        directory = os.listdir('.')

        if "stats.txt" in directory:
            call(["rm", "stats.txt"])

        call(["touch","stats.txt"])
        #above may be unnecessary...
        stats = open("stats.txt","w")
        self.player_HP = 10
        self.backpack = []
        self.equipped = ""
        stats.write( "%d\n" % self.player_HP)
        stats.write( str(self.backpack) )
        stats.write( os.linesep ) 
        stats.write( "%s" % self.equipped )
        stats.close()

        #check
        stats = open("stats.txt", "r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()


    def enter(self):
        intro = """
Welcome to the game!  This plot comes from the popular Zelda games series.  In this game you will follow the adventures of link, as he tries to remember something important...Well let's get started!  You awake in a room.
"""
                   
        print intro
        return 'links'

class Room(object):

    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()
        
    def enter(self):
        print "You misconfigured this room!!!"

class LinksRoom(Room):
    
    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()
        
    def enter(self):
        room_description = """
The room you awake in looks much like your own, however there are no windows.  You find a note on the table in front of you it reads...
 "Our hero approaches the theif!  'I'll save you Zelda!!!'  Our hero will not give up, but the theif is tricky."  The rest of the room, reminds you of home.  You get up and put on your clothes.  You see a door infront of you.  There is a rurring sound coming from the other side.  Like a large fan...  

You got clothes!!!
You got a backpack to put stuff in!!!
current HP: %d
""" % self.player_HP
        print room_description
        action = 0
        while not (action == 1):
            print "What would you like to do now?"
            print "\n1.open the door\n 2.sleep more\n 3.look around\n"
            action = int(raw_input("> "))

            if action == 1:
                print "You walk through to the next room..."
                stats = open("stats.txt", "w")
                stats.write( "%d\n" % self.player_HP)
                stats.write( str(self.backpack) )
                stats.write( os.linesep ) 
                stats.write( "%s" % self.equipped )
                stats.close()
                return 'puzzleOne'
            elif action == 2:
                print "Good night! HP restored!!!"
                self.player_HP = 10
            elif action == 3:
                print "You found a sword!!!"
                self.equipped = "master sword"
                

class PuzzleOne(Room):
    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = list(stats.readline().strip("\n"))
        self.equipped = stats.readline().strip("\n")
        stats.close()

    
       
    def enter(self):
        # room is a 5 by 5 block
        def draw_map(location):
            dead = False
            count = 0

            while not dead:
                print( ("-" * 10) + "\n" + ("| | " + "| | " + "| |") + "\n" + ("-" * 10) )
                print( ("|d| " + "| | " + "|v|") + "\n" + ("-" * 10) )
                print( ("|v| " + "| | " + "| |") + "\n" + ("-" * 10) )
                print( ("| | " + "| | " + "|v|") + "\n" + ("-" * 10) )
                print( ("| | " + "| | " + "|e|") + "\n" + ("-" * 10) )
                print( "Key: \n d: entrance door  \n v: vent \n e: exit door") 
                if count == 0:
                    print "You start at location d"
                count += 1
                print location
                print "What would you like to do?"
                print "options: \n 1. move left \n 2. move right \n 3. move down \n 4. move up"
                prompt = raw_input("> ")
                if prompt == "1":
                    location[0] -= 1
                if prompt == "2":
                    location[0] += 1
                if prompt == "3":
                    location[1] += 1
                if prompt == "4":
                    location[1] -= 1
                #consequences of moving to new location
                if location[0] <= 0 or location[1] <= 0:
                    print "You can't do that!!"
                #vents
                if "metal boots" not in self.backpack:
                    if location == [1,2] or location == [3,1] or location == [3,3]:
                        print "you got sucked up into the vent"
                        print "game over."
                        dead = True
                        sys.exit(0)
                else:
                    if location == [1,2]:
                        print "You got bow and arrows!!!"
                        self.backpack.append("bow and arrows")
                    if location == [3,1]:
                        print "You got moon tunic, shimmers with the power of the moon!!!"
                        self.backpack.append("moon tunic")
                    if location == [3,3]:
                        print "You got enhanced master sword and shield!!!"
                        self.backpack.append("E master sword")
                        self.backpack.append("sheild")
                #treasure
                if location == [1,4]:
                    print "you found treasure chest!!!"
                    print "inside is metal boots!!!"
                    self.backpack.append("metal boots")
                if location == [3,4]:
                    print "You made it out alive!!!"
                    stats = open("stats.txt", "w")
                    stats.write( "%d\n" % self.player_HP)
                    stats.write( str( self.backpack ) )
                    stats.write( os.linesep )
                    stats.write( "%s" % self.equipped )
                    stats.close()
                    return 'fightOne'

        room_description = """
You find yourself in a large room.  If you look up you see a giant fan.  There appears to be pockets of air that shoot you closer to the giant fan.
You must find a way across the room without falling into the ceiling."""
        print room_description
        
        location = [1,1]

        draw_map(location)
        return 'fightOne'
        
 
            


class FightOne(Room):
    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()


    def battle(self):
        bad_ass = False
        if "E master sword" in self.backpack:
            print "Would you like to equip your new weapons now?"
            prompt = raw_input("> ")
            if "Y" or "y" in prompt:
                print "weapons and armor equipped!!!"
                self.equipped = "E master sword"
                if "moon tunic" in self.backpack:
                    print "new tunic on...Now immune to elemental attacks!!!"
                    bad_ass = True
                    
        shadow_HP = 10
        while shadow_HP > 0:
            print "what do you do:"
            print "1. attack with sword \n 2. Defend with shield \n 3. stand their and grin"
            prompt = int(raw_input("> "))
            
            if prompt == 1:
                if self.equipped == "E master sword":
                    shadow_HP -= randint(8,50)
                else:
                    shadow_HP -= randint(3,4)
                    
                self.player_HP -= randint(1,2)
            if prompt == 2:
                if self.equipped == "E master sword":
                    print "You defend with your shield"
                    print "No HP lost"
                if bad_ass:       
                    print "Shadow link dies instantly upon touching you."
                    shadow_HP = 0
                else:
                    print "You don't have a shield!!!"
                    self.player_HP -= randint(1,4)

              
            if prompt == 3:
                if bad_ass:
                    print "Shadow link dies instantly upon touching you."
                    shadow_HP = 0
                else:
                    print "You fool..."
                    self.player_HP -= randint(5,30)
            
            print "Your current HP: %d" % self.player_HP
            print "Shadow's HP: %d" % shadow_HP
            
        
            if self.player_HP <=0:
                print "You lost...Your shadow consumes you."
                sys.exit(0)

 

    def enter(self):
        room_description = """
You enter a room.  There is a man standing in the middle.  He is holding a sword and shield.  His head is cloaked and his body is somehow always in shadow.  He charges you without hesitation
"""
        print room_description
        
        self.battle()
        stats = open("stats.txt", "w")
        stats.write( "%d\n" % self.player_HP)
        stats.write( str(self.backpack))
        stats.write( os.linesep)
        stats.write("%s" % self.equipped)
        stats.close()
        
        return 'puzzleTwo'
        

class PuzzleTwo(Room):
    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = int(stats.readline().strip("\n"))
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()
    def enter(self):
        print "You see a large clock in the center of the room."
        print "It turns into a face and grins at you."
        print "You will never see Zelda again!"
        print "The face turns into pictures."
        print "You see yourself running after Zelda's kidnapper."
        print "You start to remember what happened."
        print "You were in the middle of a great battle."
        print "And then the screen goes dark."
        print "A final face appears.  It is grinning at you."
        print "How do you plan to defeat me?"
        print "I am all that is, I am time itself."
        
        
        prompt = raw_input("The hero of time indeed...\n>")
        if "use" in prompt and "sword" in prompt:
            print "The clock disappears and a door appears, you run through it."
            return 'FinalBattle'

class FinalBattle(Room):
    def __init__(self):
        stats = open("stats.txt","r")
        self.player_HP = 35
        self.backpack = stats.readline().strip("\n")
        self.equipped = stats.readline().strip("\n")
        stats.close()
    
    def battle(self):
        bad_ass = False
        if "E master sword" in self.backpack:
            print "Would you like to equip your new weapons now?"
            prompt = raw_input("> ")
            if "Y" or "y" in prompt:
                print "weapons and armor equipped!!!"
                self.equipped = "E master sword"
                if "moon tunic" in self.backpack:
                    print "new tunic on...Now immune to elemental attacks!!!"
                    bad_ass = True
                    
        Boss_HP = 50
        while Boss_HP > 0:
            print "what do you do:"
            print "1. attack with sword \n 2. Defend with shield \n 3. stand their and grin"
            prompt = int(raw_input("> "))
            
            if prompt == 1:
                if self.equipped == "E master sword":
                    Boss_HP -= randint(8,45)
                else:
                    Boss_HP -= randint(3,4)
                
                self.player_HP -= randint(1,5)
            if prompt == 2:
                if self.equipped == "E master sword":
                    print "You defend with your shield"
                    self.player_HP -= randint(3,4)
                if bad_ass:       
                    print "Boss gets hurt upon touching you."
                    Boss_HP -= 30
                    self.player_HP -= randint(3,7)
                else:
                    print "You don't have a shield!!!"
                    self.player_HP -= randint(5,50)

              
            if prompt == 3:
                if bad_ass:
                    print "Boss gets hurt upon touching you."
                    Boss_HP -= 30
                    self.player_HP -= randint(7,15)
                else:
                    print "You fool..."
                    self.player_HP -= randint(5,30)
            
            print "Your current HP: %d" % self.player_HP
            print "Boss's HP: %d" % Boss_HP
            
        
            if self.player_HP <=0:
                print "You lost...The theif gets away with Zelda."
                sys.exit(0)

        



    def enter(self):
        print "You wake up on the floor of a room.  The theif that stole Zelda is cackling about how easily he defeated you."
        print "You wait for his guard to drop, pick up your sword and sink it into his back."
        print "He shreks with pain, 'You'll pay for that!!!'"

        self.battle()
        print "You won!"
        
    


