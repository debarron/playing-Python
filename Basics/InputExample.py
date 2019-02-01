# Create a program that
# captures your name from the
# standar input

name = raw_input("Your name please: ")
age = raw_input("Your age please: ")

age_after_10_years = int(age) + 10
age_before_10_years = int(age) - 10
year_i_was_born = 2016 - int(age)

print "Hello " + str(name) + " you're " + str(age) + " years old."
print "You'll be " + str(age_after_10_years) + " in ten years."
print "You were " + str(age_before_10_years) + " ten years ago."
print "You probably were born in " + str(year_i_was_born) + "."
