import math

def get_primes1(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list

# or better yet...

#this does not appear to work...
def get_primes2(input_list):
    return (element for element in input_list if is_prime(element))

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

