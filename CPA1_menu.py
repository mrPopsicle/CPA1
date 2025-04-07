# %%
def main_menu():
    while True:
        print("*" * 40)
        print("*" + " " * 38 + "*")
        print("*    Welcome to the Math Practice App!    *") # Change name?
        print("*" + " " * 38 + "*")
        print("*" * 40)
        print("\n")

        # Options
        print("1. Elementary School")
        print("2. High School")
        print("3. Exit")

        choice = input("Select a level: ")

        if choice == '1':
            print("You selected Elementary. Starting quiz...\n")
            import CPA1_ELEM_SECTION
            CPA1_ELEM_SECTION.math_practice_elem()
        elif choice == '2':
            print("You selected Junior High School. Starting quiz...\n")
            import CPA1_HS_SECTION2
            CPA1_HS_SECTION2.math_practice_highschool()
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

        

if __name__ == "__main__":
    main_menu()


