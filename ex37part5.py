#Now are going to learn how to send values too a generator

import math

def print_successive_primes(iterations, base=10):
    #like normal functions, a generator function
    #can be assigned to a variable

    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

def get_primes(number):
    while True:
        if is_prime(number):
           number =  yield number
        number += 1

#The assignment statement is what allows us to send to the generator
#number = yield number literally means, when a value is sent to me
#set it equal to number

#note send both sends a value to the generator and returns the value
#yielded by the generator, thus working like yield plus.

#second notice the prime_generator.send(None) line
#When using send to "start" a generator, you must send None.
#above start refers to execution of code from the first line of the 
#generator function up to the first yield statement.


#making sure to include is_prime:

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
            return True
        return False

