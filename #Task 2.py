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
        
        
        #Task 3
toppings = []
print ("Enter your favorite pizza toppings. To stop, enter 'done'.")
while True:
    topping= input ("Enter a topping:").lower()
    if topping == 'done':
        break
    toppings.append(topping)
    
    print("\nYour favorite pizza toppings are")
    for topping in toppings:
        print(topping)