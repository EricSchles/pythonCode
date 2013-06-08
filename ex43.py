class Scene(object):
    
    def enter(self):
        print "Miss configured file!!!"

class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death(Scene):
        
    def enter(self,cause):
    print cause + " So I guess you are dead.  But look at it this way:"
    print "It could be worse, you could wake up on fire."

class CentralCorridor(Scene):
    def enter(self):
        print "In this corridor you see a Gothon, standing there."
        print "If you tell it a joke, it may let you pass."
        print "Otherwise, expect certain doom."

        prompt = raw_input("> ")

        if "knock" in prompt:
            print "'Ho! What a joy!', says the Gothon."
            print "'You may pass'"
            print prompt + ".  What a funny joke!"

class LaserWeaponArmory(Scene):
    def enter(self):
        global has_bomb = False
        print "You see a giant room, in the center is a neurton bomb."
        print "It is incased in an impentrable case."
        print "In front of the case you see a number pad."
        print "The num pad has a lock symbol above it."
        print "What do you do?"

        prompt = raw_input("> ")
        if "approach" in prompt and ("num pad" in prompt or "number pad" in prompt):
            print "Enter a number.  If you get it right, you will recieve the device.  You have three tries."
            count = 0
            while count < 3:
                print "Guess a number from 1 - 10:"
                prompt = raw_input("> ")
                if prompt == 7:
                    print "You got it right!"
                    print "Received Neutron bomb!!!"
                    has_bomb = True
                    break
                else:
                    print "You have:", 2 - count,"guesses remaining"

                count += 1

class TheBridge(Scene):
    def enter(self):
        global bomb_set = False
        print "you enter a room with a bridge."
        print "Here you see a Gothon with a spear."
        if has_bomb == True:
            print "I see you have the bomb."
            print "I will kill you before you can place it!"
            print "What do you do?"
            
            prompt = raw_input("> ")
            if "fight" in prompt:
                print "You defeat the Gothon with a mighty blow."
                print "You place the bomb!!!"
                bomb_set = True
            else:
                print "The Gothon smites you"
                

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

