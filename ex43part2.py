from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured.  Subclass it and implement enter()."

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Battle(object):
    def __init__(self, monster_number):
        self.monster_number = monster_number
        self.player_HP = 10
        self.monster_HP = 5
    def enter(self):
        
        if self.monster_number > 1:
            more_than_one = True
        else:
            more_than_one = False

        defending = False
        while self.monster_number > 0:

            if self.player_HP <= 0:
                break

            if defending == True:
                print "You cannot attack this turn!!"
                defending = False

            print "Action>\n 1. attack\n 2. defend\n "
            action = raw_input("> ")

            if action == "1":
                monster_down = randint(1,5)
                self.monster_HP = self.monster_HP - monster_down
                print "You hit the monster for %d HP points!" % monster_down
                if self.monster_HP <= 0:
                    self.monster_number = self.monster_number - 1
            elif action == "2":
                print "Defensive mode!!!"
                defending = True
                recovery = randint(1,3)
                self.player_HP = self.player_HP + recovery
                print "You recovered %d HP points!" % recovery
            else:
                print "\n I did not understand that action..."
                action = "skip"
            print "\nGothon's turn\n"
            if action == "1":
                hp_down = randint(0,2)
                self.player_HP = self.player_HP - hp_down 
                print "You were hit for %d HP points" % hp_down 
            elif action == "2":
                hp_down = randint(1,3)
                self.player_HP = self.player_HP - hp_down 
                print "You were hit for %d HP points" % hp_down 
            else:
                pass
          
        if self.player_HP > 0:
            if more_than_one:
                print "congradulations, you defeated the Gothons!"
                print "(in this room)"
                return 'victory'
            else:
                print "congradulations, you defeated the Gothon!"
                print "(in this room)"
                return 'victory'
            
        else:
            print "You lost..."
            return 'failure'

class Death(Scene):
    
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if you were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
        ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
      print "The Gothons of Planet Percal #25 have invaded your ship and"
      print "destroyed your entire crew.  You are the last surviving"
      print "member and your last mission is to get the neutron destruct"
      print "bomb from the Weapons Armory, put it in the bridge, and blow"
      print "the ship up after getting into an escape pod.\n"
      print "You're running down the central corridor to the Weapons Armory"
      print "when a Gothon jumps out, red scaly skin, dark grimy teeth, and"
      print "evil clown costume flowing around his hate filled body."
      print "He's blocking the door to the Armory and about to pull a weapon"
      print "to blast you."

      action = raw_input("> ")

      number_of_Gothons = 1

      battle = Battle(number_of_Gothons)


      if action == "cheat":
          return 'cheat'
      
      if "fight" in action:
          result = battle.enter()
      if result == 'victory':
          print "You defeat the Gothon with a shot to the head!"
          print "Then you jump through the Weapon Armory door."
          return 'laser_weapon_armory'
      if result == 'failure':
          print "The Gothon eats you alive..."
          return 'death'
      else:
          print "something went horribly wrong..."

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan"
        print "the room for more Gothons that might be hiding.  It's dead"
        print "quiet, too quiet.  You stand up and run to the far side of"
        print "the room and find the neutron bomb in its container.  There's"
        print "a keypad lock on the box and you need the code to get the"
        print "bomb out. If you get the code wrong 10 times then the lock"
        print "closes forever and you can't get the bomb.  The code is 3"
        print "digits."
        
        code = "%d%d%d" % (1,1,1)#(randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        
        if guess == "cheat":
            return 'cheat'

        guesses = 0

        while guess != code and guesses < 9:
            print "BZZZZZZZZEDDD!"
            guesses += 1
            if guess < code:
                print "higher"
            elif guess > code:
                print "lower"
            else:
                pass
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting"
            print "gas out.  You grab the neutron bomb and run as fast as"
            print "you can to the bridge where you must place it in the"
            print "right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a"
            print "sickening melting sound as the mechanism is fused"
            print "together.  You decide to sit there, and finally"
            print "the Gothons blow up the ship from their ship and"
            print "you die."
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "cheat":
            return 'cheat'

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right the back killing you."
            print "As you die you see another Gothon frantically try"
            print "try to disarm the bomb.  You die knowing they will"
            print "probably blow up when it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then"
            print "carefully place the bomb on the floor, point your"
            print "your blaster at it.  You then jump back through"
            print "the door, punch the close button and blast the lock"
            print "so the Gothons can't get out.  Now that the bomb is"
            print "placed you run to the escape pod to get off this tin"
            print "can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems"
        print "like hardly any Gothons are on the ship, so your run is"
        print "is clear of interference.  You get to the chamber with"
        print "the escape pods, and now need to pick one to take.  Some"
        print "of them could be damaged but you don't have time to look."
        print "There's 5 pods, which one do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod#]> ")

        if guess == "cheat":
            return 'cheat'


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you"
            print "look back and see your ship implode then explode like"
            print "a bright star, taking out the Gothon ship at the same"
            print "time.  You won!"
            return 'finished'

class Congrads(Scene):
    def enter(self):
        print "Congradulations!!!"
        exit(0)

class Cheat(Scene):
    def enter(self):
        print "Well, if you are going to cheat..."
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished':Congrads(), 
        'cheat': Cheat()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

