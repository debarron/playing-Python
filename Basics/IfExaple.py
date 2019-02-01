# The use of if statements
# Write a program that can tell
# if you are and adult

age = int(raw_input("Tell me your age: "))

if( age < 21 ):
  print "You can not drink"
elif ( age < 31):
  print "Let's have beer!"
else:
  print "Let's drink anything!"
