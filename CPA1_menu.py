# %%
def main_menu():
    while True:
        print("*" * 32)
        print("*" + " " * 30 + "*")
        print("* Welcome to the Math Practice App! *") # Change name?
        print("*" + " " * 30 + "*")
        print("*" * 32)
        print("\n")

        # Options
        print("1. Grade School")
        print("2. Elementary School")
        print("3. Senior High School")
        print("4. Exit")

        choice = input("Select a level: ")

        if choice == '1':
            print("You selected Grade School. Staring quiz...\n")
        elif choice == '2':
            print("You selected Elemenatry. Starting quiz...\n")
        elif choice == '3':
            print("You selected Senior High School. Starting quiz...\n")
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main_menu()


