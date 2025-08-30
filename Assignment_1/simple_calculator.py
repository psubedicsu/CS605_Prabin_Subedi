print("\nWelcome to the Simple Calculator")
a='yes'
while (a=="yes"):
    while True:
        n1= input("\nEnter the first number: ")
        if n1.isdigit():
            n1 = int(n1)
            break
        else:
            print("\nInvalid input. Enter an integer.")
    while True:
        n2= input("\nEnter the second number: ")
        if n2.isdigit():
            n2 = int(n2)
            break
        else:
            print("\nInvalid input. Enter an integer.")
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    op=int(input("\nEnter the operation number: "))
    if op == 1:
        print(f"\nResult: {n1} + {n2} = {n1 + n2}")
    elif op == 2:
        print(f"\nResult: {n1} - {n2} = {n1 - n2}")
    elif op == 3:
        print(f"\nResult: {n1} * {n2} = {n1 * n2}")
    elif op == 4:
        print(f"\nResult: {n1} / {n2} = {'Error: Cannot divide by zero' if n2 == 0 else n1 / n2}")
    else:
        print("\nInvalid operation!!!")
    a = input("\nDo you want to perform another calculation? (yes/no): ").lower()

print("\nGoodbye!\n")
