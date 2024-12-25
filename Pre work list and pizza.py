#Task 1.
numbers = list(range(1,11))
print(numbers)
#creation of main list
squares = [value**2 for value in range(1,11)]
#simplified List Comprehension code
print(squares)
"\n"
#Task 2.
number = int(input("Enter a number"))
remainder = number % 2
# % divide by 2
if (remainder ==0):
    print(number,"is an even number")
else:
    print(number," is an odd number")
# input number in terminal, press enter. Response = 3 is an odd number
"\n"
#Task 3
#creating question for user, followed by input function, and then append which will apply for second part of list.
toppings = []
print ("Enter your favorite pizza toppings. To stop, enter 'done'.")
while True:
    topping= input ("Enter a topping:").lower()
    if topping == 'done':
        break
    toppings.append(topping)
    # question has been asked to user, next will be toppings response, in form of a list + "for loop"
    print("\nYour favorite pizza toppings are")
    toppings = ['pepperoni', 'sausage', 'extra cheese']
    for topping in toppings:
        print(topping)
        #finish with entering 'done'