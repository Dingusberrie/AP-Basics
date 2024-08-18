# Ask user for width and loop until they
# enter a number that is more thank zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    length = num_check("length: ")
    cost = num_check("Cost: ")

    # Calculate area / perimeter
    area = width * length
    perimeter = 2 * (width + length)
    price =  cost * perimeter

    # Diplay output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price. ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")
