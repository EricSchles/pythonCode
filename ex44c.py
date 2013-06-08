class Parent(object):
    
    def altered(Self):
        print "PARENT altered()"

class Child(Parent):
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

