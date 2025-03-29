import random
from CPA1_HS_SECTION2 import get_user_input


def algebra_menu():
    """Main menu for algebra topics."""

    print("\nWelcome to the Algebra Section!")

    while True:
        print("\nSelect a topic:")
        print("1. Linear Equations")
        print("2. Quadratic Equations")
        print("3. System of Equations")
        print("4. Rational Expressions")
        print("6. Factoring Trinomials")
        print("7. Rules of Exponents")
        print("8. Exit")

        choice = input("Enter your choice: ")

        while True:
            if choice == "7":
                print("You selected Rules of Exponent. Starting quiz...\n")
                answer, string_answer = rules_of_exponents()
                user_answer = get_user_input()
                while user_answer != answer and str(user_answer) != str(string_answer):
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")




            repeat = input("Would you like to continue? (y/n): ").strip().lower()
            if repeat == "n":
                break
            elif repeat == "y":
                continue
            else:
                print("Invalid choice. Please select a valid option.\n")
                continue
 






def linear_equation():
    """generate a linear equation question"""
    a = random.randint(1, 10)
    b = random.randint(5, 25)
    c = random.randint(1, 100)
    d = random.randint(1, 70)
    equation_type = random.choice(["ver1", "ver2", "distributive"])
    if equation_type == "ver1":
        print(f"{a}x + {b} = {c} + {d}x")
        x = (a -d) / (c - b)
    if equation_type == "ver2":
        print(f"{a}x - {b} = {c} - {d}x")
        x = (a + d) / (c + b)
    else:
        print(f"{a}({b}x + {c}) = {d}x")
        x = (d - (a*b)) / (a*c)
    print(f"Solve for x:\n {equation_type}")
    return x

def quadratic_equation():
    """generate a quadratic equation question"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    print(f"Solve the following equation:")
    print(f"{a}x^2 + {b}x + {c} = 0")
    x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f"Solve for x:\n {x}")
    return x

def system_of_equations():
    """generate a system of equations question"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    f = random.randint(1, 10)
    print(f"Solve the following system of equations:")
    print(f"{a}x + {b}y = {c}")
    print(f"{d}x + {e}y = {f}")
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    print(f"Solve for x and y:\n {x}, {y}")
    return x, y

def rational_expression():
    """generate a rational expression question"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    print(f"Simplify the following rational expression:")
    equation_type = random.choice(["ver1", "ver2", "ver3", "ver4"])
    if equation_type == "ver1":
        print(f"{a}/{b} + {c}/{d}")
        x = (a * d + b * c) / (b * d)
    return x

















 
def factoring_trinomials():
    """generate a factoring trinomials question"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    print(f"Factor the following trinomial:")
    print(f"{a}x^2 + {b}x + {c}")
    x = (a * d + b * c) / (b * d)
    return x






















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




    




if __name__ == "__main__":
    algebra_menu()
    