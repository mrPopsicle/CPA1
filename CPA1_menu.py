# %%
def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("||" + " " * 56 + "||")
        print("||" + " " * 13 + "👾  M A T H   I N V A D E R S  👾" + " " * 13 + "||")
        print("||" + " " * 56 + "||")
        print("=" * 60)

        print(r"""
                           .
                           |
                           ^
                          / \
                         /___\
                        |=   =|
                        |     |
                        |     |
                       /|##!##|\
                      / |##!##| \
                     /  |##!##|  \
                    |  / ^ | ^ \  |
                    | /  ( | )  \ |
                    |/   ( | )   \|
                        ((   ))
                       ((  :  ))
                       ((  :  ))
                        ((   ))
                         (( ))
                          ( )
                           .
                           .
                           .
                    """) 
        
        print("              [1] Elementary School")
        print("              [2] High School")
        print("              [3] Exit\n")

        choice = input(">> Select a level (1-3): ")

        if choice == '1':
            print("\n🚀 Launching Elementary Mission...\n")
            import CPA1_ELEM_SECTION
            CPA1_ELEM_SECTION.math_practice_elem()
        elif choice == '2':
            print("\n🛸 Launching High School Mission...\n")
            import CPA1_HS_SECTION2
            CPA1_HS_SECTION2.math_practice_highschool()
        elif choice == '3':
            print("\n👋 Game Over. Thanks for playing Math Invaders!")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main_menu()


