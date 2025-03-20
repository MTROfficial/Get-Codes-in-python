class User:
    def __init__(self, first_name, middle_name, last_name, email, password, mobile_number, address):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
        self.mobile_number = mobile_number
        self.address = address


def Add():
    print("\n\n\ndef addition():")
    print("print('Welcome to Addition Calculator')")
    print("num1 = float(input('Enter first number: '))")
    print("num2 = float(input('Enter second number: '))")
    print("sum_result = num1 + num2")
    print("print(f'The sum of {num1} and {num2} is: {sum_result}')")
    print("addition()\n\n\n")

    
def Sub():
    print("\n\n\ndef subtraction():")
    print("print('Welcome to Subtraction calculator')")
    print("num1 = float(input('Enter first number: '))")
    print("num2 = float(input('Enter second number: '))")
    print("subtraction_result = num1 - num2")
    print("print(f'The subtraction of {num1} and {num2} is: {subtraction_result}')")
    print("subtraction()\n\n\n")

def Multi():
    print("\n\n\ndef multiplication():")
    print("print('Welcome to Multiplication calculator')")
    print("num1 = float(input('Enter first number: '))")
    print("num2 = float(input('Enter second number: '))")
    print("multiplication_result = num1 * num2")
    print("print(f'The multiplication of {num1} and {num2} is: {multiplication_result}')")
    print("multiplication()\n\n\n")

def Divide():
    print("\n\n\ndef division():")
    print("print('Welcome to Division calculator')")
    print("num1 = float(input('Enter first number: '))")
    print("num2 = float(input('Enter second number: '))")
    print("division_result = num1 / num2")
    print("print(f'The subtraction of {num1} and {num2} is: {division_result}')")
    print("division()\n\n\n")



if __name__ == "__main__":
    while True:
        print("\n===== Welcome Get python code Application =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            Add()
        elif choice == '2':
            Sub()
        elif choice == '3':
            Multi()
        elif choice == '4':
            Divide()
        elif choice == '5':
            print("Thanks for using our application, Bye Take care!")
            break
        else:
            print("Invalid choice. Please enter again.")

