import random
import math
from CPA1_HS_SECTION2 import get_user_input




def linear_equation():
    """Generate a linear equation question"""
    a = random.randint(1, 10)
    b = random.randint(5, 25)
    c = random.randint(1, 100)
    d = random.randint(1, 70)
    
    equation_type = random.choice(["ver1", "ver2", "distributive"])
    
    if equation_type == "ver1":
        print(f"Solve for x: {a}x + {b} = {c} + {d}x")
        
        x = (c - b) / (a - d)
    elif equation_type == "ver2":
        print(f"Solve for x: {a}x - {b} = {c} - {d}x")
        
        x = (c + b) / (a + d)
    else:  
        print(f"Solve for x: {a}({b}x + {c}) = {d}x")
        
        x = (a * c) / (d - (a * b))
    
    return x


def quadratic_equation():
    """Generate a quadratic equation question"""
    
    while True:
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            break
    
    print(f"Solve for x: {a}x^2 + {b}x - {c} = 0 (find the positive root)")
   
    x = (-b + (b**2 + 4*a*c)**0.5) / (2*a)
    return x


def system_of_equations():
    """Generate a system of equations question"""
   
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    
   
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    
    e = a * x + b * y
    f = c * x + d * y
    
    print("Solve the system:")
    print(f"{a}x + {b}y = {e}")
    print(f"{c}x + {d}y = {f}")
    
    return x, y


def rational_expression():
    """Generate a rational expression question"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    print(f"Simplify: {a}/{b} + {c}/{d}")
    
    
    numerator = a * d + b * c
    denominator = b * d
    
   
    
    gcd = math.gcd(numerator, denominator)
    result = numerator / denominator
    
    return result


def factoring_trinomials():
    """Generate a factoring trinomials question"""

    m = random.randint(1, 10)
    n = random.randint(1, 10)
    
    a = 1
    b = m + n
    c = m * n
    
    print(f"Factor the trinomial: {a}x^2 + {b}x + {c}")
    print("Enter your answer as the value of the smaller root.")
 
    return min(-m, -n)



def rules_of_exponents():
    """generate exponents question with random questions about
    different rules of exponents
    """
    base = random.randint(5, 100)
    power = random.randint(1, 10)
    base1 = random.randint(5, 100)
    power1 = random.randint(1, 10)

    print(f"Simplify the following expression:")
    equation_type = random.choice(["product", "quotient", "power", "product_rule", "quotient_rule"])


    if equation_type == "product":
        print(f"{base}^{power} * {base}^{power1}")
        exponent_sum = power + power1
        string_answer = f"{base}^{exponent_sum}"
        x = base ** (power + power1)
    elif equation_type == "quotient":
        print(f"{base}^{power} / {base}^{power1}")
        exponent_diff = power - power1
        if exponent_diff < 0:
            string_answer = f"1/{base}^{abs(exponent_diff)}"
        else:
            string_answer = f"{base}^{exponent_diff}"
        x = base ** (power - power1)
    
    elif equation_type == "power":
        print(f"({base}^{power})^{power1}")
        exponent_product = power * power1
        string_answer = f"{base}^{exponent_product}"
        x = base ** (power * power1)
    elif equation_type == "power":
        print(f"({base}^{power})^-{power1}")
        exponent_diff = power - power1
        string_answer = f"{base}^{exponent_diff}"
        x = base ** (power - power1)
    
    elif equation_type == "product_rule":
        print(f"({base}^{power} * {base1}^{power1})")
        exponent_sum = power + power1
        string_answer = f"{base}^{exponent_sum}"
        x = base ** (power + power1)
    elif equation_type == "quotient_rule":
        print(f"(({base} / {base1})^{power})")
        answer = base ** power / base1 ** power
        string_answer = f"{base}^{power} / {base1}^{power}" 
        x = answer

    
    return x, string_answer



def algebra_menu():
    """Main menu for algebra topics."""

    print("\nWelcome to the Algebra Section!")

while True:
    print("\nSelect a topic:")
    print("1. Linear Equations")
    print("2. Quadratic Equations")
    print("3. System of Equations")
    print("4. Rational Expressions")
    print("5. Factoring Trinomials") 
    print("6. Rules of Exponents")    
    print("7. Exit")

    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            print("You selected Linear Equations. Starting quiz...\n")
            answer = linear_equation()
            user_answer = get_user_input()
            while user_answer != answer and str(user_answer) != str(answer):
                print("Incorrect. Try again.")
                user_answer = get_user_input()
            print("Correct!\n")
        
        elif choice == "2":
            print("You selected Quadratic Equations. Starting quiz...\n")
            answer = quadratic_equation()
            user_answer = get_user_input()
            while user_answer != answer and str(user_answer) != str(answer):
                print("Incorrect. Try again.")
                user_answer = get_user_input()
            print("Correct!\n")
        
        elif choice == "3":
            print("You selected System of Equations. Starting quiz...\n")
            answer_x, answer_y = system_of_equations()
            print("Enter the value of x:")
            user_answer_x = get_user_input()
            print("Enter the value of y:")
            user_answer_y = get_user_input()
            while (user_answer_x != answer_x or user_answer_y != answer_y) and \
                (str(user_answer_x) != str(answer_x) or str(user_answer_y) != str(answer_y)):
                print("Incorrect. Try again.")
                print("Enter the value of x:")
                user_answer_x = get_user_input()
                print("Enter the value of y:")
                user_answer_y = get_user_input()
            print("Correct!\n")
        
        elif choice == "4":
            print("You selected Rational Expressions. Starting quiz...\n")
            answer = rational_expression()
            user_answer = get_user_input()
            while user_answer != answer and str(user_answer) != str(answer):
                print("Incorrect. Try again.")
                user_answer = get_user_input()
            print("Correct!\n")
        
        elif choice == "5":
            print("You selected Factoring Trinomials. Starting quiz...\n")
            answer = factoring_trinomials()
            user_answer = get_user_input()
            while user_answer != answer and str(user_answer) != str(answer):
                print("Incorrect. Try again.")
                user_answer = get_user_input()
            print("Correct!\n")

        elif choice == "6":
            print("You selected Rules of Exponent. Starting quiz...\n")
            answer, string_answer = rules_of_exponents()
            user_answer = get_user_input()
            while user_answer != answer and str(user_answer) != str(string_answer):
                print("Incorrect. Try again.")
                user_answer = get_user_input()
            print("Correct!\n")
        
        elif choice == "7":
            print("Exiting Algebra section. Goodbye!")
            break
    
        else:
            print("Invalid choice. Please select a valid option.\n")
            continue




        repeat = input("Would you like to continue? (y/n): ").strip().lower()
        if repeat == "n":
            break
        elif repeat == "y":
            continue
        else:
            print("Invalid choice. Please select a valid option.\n")
            continue
 



    




if __name__ == "__main__":
    algebra_menu()
    