#ITERABLES

#When you create a list, you can read its items one by one, and its called
#iteration
mylist = [1,2,3]
for i in mylist:
    print(i)

#output: out, 1,2,3
#mylist is an iterable.  
#When you use a list comprehension, you create a list and so an iterable:

mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

#Every you can use "for...in..." on is an iterable: lists, strings, files,etc
#With iterables you can read them as much as you wish, storing the values in
#memory.  If you have a lot of values, you may not want to do this.

# GENERATORS

#Generators are iterators, but you can only iterate over them once.  
#It's because they do not store values in memory, they generate them on the
#fly.

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

#outputs 0,1,4
#It appears the same as the list, except for the use of () instead of []
#However you cannot perform "for in mygenerator" a second time.

#YIELD

#Yield is a keyword that is used like return, expect the function will return
#a generator.

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)

#To master yield, you must realize that when you call the function, the code
#you have written in the function body does not run.  The function only 
#returns the generator object.

#Then, your code will be run each time the for uses the generator.

#As a second example:
#Controlling a generator exhaustion
class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            return "$100"
#play around with this code.
#See what happens when crisis is set to True.
