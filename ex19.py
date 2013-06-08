
#this is the main function of the script, it is called 4 times
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#here we show passing a function numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#here we show passing a function variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#here we show passing a function mathematical expressions
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#here we show passing a combination of math and variables.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
