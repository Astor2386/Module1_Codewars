#Favorite Movies Project
#Create an empty dictionary to hold movies
movies = {}
# 3 functions to create, add movie, remove movie, view movies
def add_movie():
    """add new movie to dictionary"""
    title = input("Enter the movie title: ")
    genre = input("Enter the genre type: ")
    rating = input("Enter the rating: ")
    director = input("Enter the director: ")
    movies[title] = {'genre': genre, 'rating': rating,
                     'director': director}
    print("movie added successfully.")
    
def remove_movie():
    """Remove a movie from the dictionary"""
    title = input("Enter the title of the movie to remove: ")
    if title in movies:
        del movies[title]
        print("Movie removed successfully.")
    else:
        print("That movie is not in your list.")
        
def view_movies():
    """Display all movies in the dictionary."""
    if not movies: 
        print("You have no movies in your list.")
    else:
        for title in movies.keys():
            info = movies[title]
            print("{0} - Genre: {1}, Rating:{2}, Director: {3}".format(title, info['genre'], info['rating'], info['director']))
            
#main loop to run program
    while True:
        print("\n1. Add a movie")
        print("2. Remove a movie")
        print("3. View movies")
        print("4. Exit")
        choice = input("Choose an option:")
        
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