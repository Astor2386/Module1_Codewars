weather = input("Is it sunny or rainy?").lower()
mood = input("Are you happy or tired?").lower()

if weather == "sunny" and mood == "happy":
    print("Go for a hike!")
elif weather == "rainy" or mood == "tired":
    print("Relax indoors.")
else:
    print("Relax indoors.")