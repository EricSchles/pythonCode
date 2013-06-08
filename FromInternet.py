##mystring = 'hho'
##
##char_count = dict()
##for char in mystring:
##    count = char_count.get(char, 0)
##    print count
##    count += 1
##    print count
##    char_count[char] = count
##    print char_count
##print char_count
##
##

things = dict()

count = things.get("h",0)
print things.get("h",0)
count += 1
print count
things["h"] = count
print things.get("h",0)
print things
