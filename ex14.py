from sys import argv

script = argv
user_name =argv
prompt ='>'

print  ("Hi %s , I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questons.")
print ("Do you like me %s?" % user_name)
likes = int (raw_input(prompt))

print ("Where do you live %s?" % user_name)
lives = int (raw_input(prompt))

print ("What kind of computer do you have?")
computer = int (raw_input(prompt))

print ("""
        Alight, so you said %r about liking me.
        You live in %r. Not sure where that is.
        And you have a %r computer. Nice.
        """ % (likes, lives, computer))
