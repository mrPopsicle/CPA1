"""This file contains the code for the submenu for Trigonometry."""

import random
import math
from fractions import Fraction


def trigonometry_menu():
    """Main menu for trigonometry topics."""
    print("\nWelcome to the Trigonometry Section!")

    while True:
        print("\nSelect a topic:")
        print("1. Unit Circle")
        print("2. Right Triangles")
        print("3. Trignometric Identities")
        print("4. Inverse Trigonometric Functions")
        print("5. Trigonometric Equations")
        print("6. Trigonometric Functions")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("You selected Unit Circle. Starting quiz...\n")
            unit_circle()
        elif choice == "2":
            print("Right Triangles. Starting quiz...\n")
        elif choice == "3":
            print("Trignometric Identities. Starting quiz...\n")
        elif choice == "4":
            print("Inverse Trigonometric Functions. Starting quiz...\n")
        elif choice == "5":
            print("Trigonometric Equations. Starting quiz...\n")
        else:
            print("Thank you for playing! Goodbye!")
            break
        


    
if __name__ == "__main__":
    trigonometry_menu()