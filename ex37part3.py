#here's a simple generator function:

def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print(value)

#Code produces no output because all values already iterated through
our_generator = simple_generator_function()

next(our_generator)
next(our_generator)
next(our_generator)

#however if you run in active mode (calling python from the terminal)
#and then define a new variable our_generator = simple_generator_function()
#you are effectively instantiating a new copy of the function
#And thus next(our_generator) can be called three times and will produce:
#1
#2
#3
