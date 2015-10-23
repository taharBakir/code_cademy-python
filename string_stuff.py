#Print a
s="Hella"[4]
print s

#Print the length of the string
parrot = "Norwegian Blue"
print len(parrot)

#Print the string in lower case
parrot = "Norwegian Blue"
print parrot.lower()

#Print the string in upper case
parrot = "norwegian blue"
print parrot.upper()

#toString
pi = 3.14
print str(pi)


#Methods that use dot notation only work with strings.
#On the other hand, len() and str() can work on other data types.
ministry = "The Ministry of Silly Walks"
print len(ministry)
print ministry.upper()

print "Spam\n" + "and\n" + "eggs"

print "The value of pi is around " + str(3.14)

'''The % operator after a string is used to combine a string with variables.
The % operator will replace a %s in the string with the string variable that comes after it.
'''

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
