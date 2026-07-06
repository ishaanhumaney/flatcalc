import math

def calculate_expression(expr):
    expr = expr.replace('^', '**')
    return eval(expr, {"__builtins__": None}, {
        "math": math,
        "sqrt": math.sqrt,
        "root": lambda x, n: x ** (1/n)
    })

def show_instructions():
    print("=== HOW TO USE THE CALCULATOR ===")
    print("1. Standard Math (BODMAS): Use +, -, *, /")
    print("   Example: 10 + 2 * (5 - 3)  -> Result: 14")
    print("2. Square Root: Use sqrt(number)")
    print("   Example: sqrt(25)          -> Result: 5.0")
    print("3. Custom Roots: Use root(number, n)")
    print("   Example: root(8, 3)        -> Result: 2.0 (Cube root of 8)")
    print("4. Exponents: Use ^")
    print("   Example: 2^3               -> Result: 8")
    print("=================================\n")

def main():
    print("--- Python Calculator ---")
    show_instructions()
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("calc> ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank You for visiting, Please visit again!")
            break
            
        if not user_input:
            continue
            
        try:
            allowed_chars = set("0123456789+-*/().^sqrtob ,")
            if not set(user_input.lower()).issubset(allowed_chars):
                print("Error: Invalid characters detected.")
                continue
                
            result = calculate_expression(user_input)
            print(f"= {result}\n")
            
        except ZeroDivisionError:
            print("Error: Division by zero.\n")
        except Exception:
            print("Error: Invalid expression.\n")

if __name__ == "__main__":
    main()
