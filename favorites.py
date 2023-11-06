from clear import clear


def add_to_favorites(movie, date, genre):
    with open("favorites_list.txt", "a") as file:
        file.write(str(movie) + " " + "(" + str(date) + ") Genre: " + str(genre) + "\n")
    print("Movie added to favorites!")


def remove_all():
    option = input("Are you sure you want to clear all? (This will clear the whole file"
          "(y/n)")
    if option.lower() == 'y':
        with open("favorites_list.txt", 'w') as file:
            file.write('')
    elif option.lower() == 'n':
        return
    else:
        print("Incorrect Option")



def remove_from_favorites(movie_number):
    with open("favorites_list.txt", "r") as file:
        favorites = file.readlines()

    if 1 <= movie_number <= len(favorites):
        del favorites[movie_number - 1]
        with open("favorites_list.txt", "w") as file:
            file.writelines(favorites)
        print("Movie removed from favorites!")
        clear()
    else:
        print("Invalid movie number. Please enter a valid number.")


def display_favorites():
    show_menu = True  # Flag to manage re-display

    while show_menu:
        with open("favorites_list.txt", "r") as file:
            favorites = file.readlines()

        if not favorites:
            print("Your favorites list is empty.")
            show_menu = False

        print("Your Favorites List:")
        print("-" * 30)  # Adding a separator
        for idx, movie in enumerate(favorites, start=1):
            print(f"{idx}. {movie.strip()}")
            print("-" * 30)  # Adding a separator after each movie

        user_choice = input(
            "Enter 'm' to go back to the main menu or 'd' to delete a movie: ")
        if user_choice.lower() == 'm':
            clear()
            show_menu = False
        elif user_choice.lower() == 'c':
            remove_all()
        elif user_choice.lower() == 'd':
            if not favorites:
                clear()
                print("Your favorites list is empty. Nothing to delete.\n")
            else:
                movie_number = int(input("Enter the movie number to delete: "))
                remove_from_favorites(movie_number)
        else:
            print(
                "Invalid choice. Please enter 'm' to return to the main menu "
                "or 'd' to delete a movie.")