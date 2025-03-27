# Part the course "Instroduction to Github Copilot" on Codecademy

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

""" 
    Prompts the user for a non-negative integer and returns it. 
    Keeps prompting until a valid non-negative integer is provided. 
""" 
def get_user_input():
    while True:
        try:
            user_input = int(input("Enter a non-negative integer: "))
            if user_input < 0:
                raise ValueError
            return user_input   
        except ValueError:  
            print("Invalid input. Please enter a non-negative integer.")
            continue

def main():
    user_input = get_user_input()
    print(f"The factorial of {user_input} is {factorial(user_input)}")  

if __name__ == "__main__":
    main()