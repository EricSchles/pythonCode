class Eric(object):
    
    def __init__(self,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight

    def play_guitar(self):
        if self.age > 16 and self.age < 24:
            print "Eric is okay at this..."
            print "But he could be better"

    def see_friends(self,friend_name):
        print "Eric would love to see %s!!" % friend_name

    def sleep(self):
        print "Eric sleeps pretty well..."


    def reading(self):
        print "Eric loves to read!"

class NYU_Eric(Eric):
    
    def __init__(self,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight

    def play_guitar(self):
        print "Eric doesn't have time for guitar anymore..."

    def see_friends(self,friend_name):
        print "Eric would love to see %s!! But cannot..." % friend_name
        print "Stupid NYU..."


    def sleep(self):
        print "Eric barely sleeps well..."



eric_before = Eric(22,"6'", 200)
eric_now = NYU_Eric(26,"6'",205)


print "Eric before NYU..."
eric_before.play_guitar()
eric_before.see_friends("noam")
eric_before.reading()
eric_before.sleep()

print "Eric after NYU.."

eric_now.play_guitar()
eric_now.see_friends("noam")
eric_now.reading()
eric_now.sleep()

