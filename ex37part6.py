#Now we are going to learn about itertools!

import itertools

horses = [1,2,3,4]
races = itertools.permutations(horses)
#this prints out the object info for races
print(races)
#this prints out all the permutations of 1,2,3,4
print(list(itertools.permutations(horses)))

#the reason we should you this is to understand the advanced uses of
#iteration.
