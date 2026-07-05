try:
    number = int(input("Enter a number: "))

    if number == 0:
        print("The number is zero.")
    elif number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Please enter a valid number.")