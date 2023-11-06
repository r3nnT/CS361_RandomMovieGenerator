#***********************************************
# CS361 Project
# Tyler Renn
#***********************************************

#Imports
import RandomMovie
import SearchMovie
from favorites import display_favorites
from clear import clear


#Initial Welcome page
def welcome():
    print("Welcome!")
    print("        ___")
    print("       [|   |=|{)__")
    print("        |___| \/   )")
    print("         /|\      /|")
    print("        / | \     | |")

    print("\nThis program will help you find what movie to watch when nothing "
          "comes to mind!\n")
    print("Features:\n"
          "-Input certain criteria based on your own interests!\n"
          "-One movie will be generated at a time, option to randomize "
          "again if needed\n"
          "-You can input all, some or no criteria based on your needs\n"
          "-Option to mark a movie as your favorite to add it to your "
          "list of a must-watch!\n"
          "-(More features to come!)\n\n")


#Main menu display
def main_menu():
    print("What would you like to do today?")
    print("1. Find a totally random movie for me (Loading time occurs)")
    print("2. Search for a specific movie (Loading time occurs)")
    print("3. Movies Watched (COMING SOON!)")
    print("4. Favorites")
    print("5. More options (COMING SOON)")
    print("6. EXIT")


#Simulates login
def login():
    name = input("What should we call you?: ")
    print(f"Hi {name}!\n")
    return name


#Defined the option call for the main menu
def options_input():
    while True:
        option = input("\nWhat would you like to do today? (1-6): ")

        try:
            number = int(option)
            if 1 <= number <= 6:
                return number
            else:
                print("Not correct")
        except ValueError:
            print("Please Input a valid number")


#Executes the option call
def menu_options():
    user = login()

    while True:
        main_menu()
        option = options_input()

        if option == 1:
            clear()
            print("THANKS FOR BEING ADVENTUROUS\nHere is a totally random "
                  " movie along with some details!")
            RandomMovie.movie_details()

            while True:
                internal_option = input(
                    "Would you like to generate another movie? (y/n): ")

                if internal_option.lower() == 'y':
                    clear()
                    print("Another Movie coming up!")
                    RandomMovie.movie_details()
                elif internal_option.lower() == 'n':
                    clear()
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")

        elif option == 2:
            # Code for option 2
            clear()
            print("YOUR PATH HAS BEEN CHOSEN\n")
            SearchMovie.movie_details()

            while True:
                internal_option = input(
                    "Would you like to search for another movie? (y/n): ")

                if internal_option.lower() == 'y':
                    clear()
                    print("Another Movie coming up!")
                    SearchMovie.movie_details()
                elif internal_option.lower() == 'n':
                    clear()
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
        # Include code for other options (3-6)

        elif option == 4:
            clear()
            display_favorites()

        elif option == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    welcome()
    menu_options()
