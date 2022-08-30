def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    return x / y


print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:

    choice = input("Enter choice: ")


    if choice in ('1', '2', '3', '4'):
        A = float(input("Enter the Value of A: "))
        B = float(input("Enter the value of B: "))

        if choice == '1':
            print(A, "+", B, "=", add(A, B))

        elif choice == '2':
            print(A, "-", B, "=", subtract(A, B))

        elif choice == '3':
            print(A, "*", B, "=", multiply(A, B))

        elif choice == '4':
            print(A, "/", B, "=", divide(A, B))
        
        next_calculation = input("Perform another task? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Invalid Input")