#main.py
from f_vidoes import add_movie, remove_movie, view_movies

#main loop
while True:
    print("\n1. Add a movie")
    print("2. Remove a movie")
    print("3. View movies")
    print("4. Exit")
    choice = input("Choose an option: ")
        
    if choice == '1':
            add_movie()
    elif choice == '2':
            remove_movie()
    elif choice == '3':
            view_movies()
    elif choice == '4':
         print("Goodbye!")
         break
    else:
        print("Invalid option. Please try again.")