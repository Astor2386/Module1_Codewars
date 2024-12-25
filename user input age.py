#Practice
# Ask the user their age using input
age = input("what is your age? ")
age = int(age)

if age <13:
    print("\nI am a child!")
elif 13 <= age < 20:
    print ("\n I'm a teenager!")
else:
    print("\nI'm an adult.")