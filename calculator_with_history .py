HISTORY_FILE = "calculation_history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            history = file.readlines()
            if not history:
                print("No calculation history found.")
            else:
                print("Calculation History:")
                for line in history:
                    print(line.strip())
    except FileNotFoundError:
        print("No calculation history found.")

def clear_history():
    open(HISTORY_FILE, "w").close()
    print("Calculation history cleared.")

def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")    

def calculator():
    print("Welcome to the Calculator with History!")
    print("Type 'history' to view calculation history , type 'clear' to clear history or 'exit' to quit.")
    
    while True:
        user_input = input("Enter a mathematical expression: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == 'history':
            show_history()
            continue
        elif user_input.lower() == 'clear':
            clear_history()
            continue
    
        
        try:
            # Evaluate the mathematical expression
            result = eval(user_input)
            print(f"Result: {result}")
            save_to_history(user_input, result)
        except Exception as e:
            print(f"Error: {e}. Please enter a valid mathematical expression.")
if __name__ == "__main__":
    calculator()
