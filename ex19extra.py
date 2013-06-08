def FunFunc(first, second):
    print "This function doesn't do very much..."
    print "It just tells you the variables contents."
    print "Check it out: %r, %r" % (first,second)
    print "Are the values for the two variables this function takes."
    

print "Here we pass in some strings:"
FunFunc("five","six")

print "Now we will play with numbers:"
FunFunc(5,6)

print "Now we will play with math:"
FunFunc(5+6,5+7)

print "Now we will play with booleans:"
FunFunc(True,False)

print "Now we will use our function a different way:"
thisMany = 5
for i in range(thisMany):
    FunFunc(i,i+1)

print "I know I'm not supposed to know about looping already, but w/e"
print "I guess I'll do something with math again, borrrrriiinnnggg:"
FunFunc(45/7,57%6)

print "Time to work with exponents!"
FunFunc(5**8,7)

print "I should really think about doing something else..."
FunFunc("hi"*5,"ho"+" weeee")

print "Only two left..."
FunFunc("Final", "countdown")

print "The end"
FunFunc("the", "end")


