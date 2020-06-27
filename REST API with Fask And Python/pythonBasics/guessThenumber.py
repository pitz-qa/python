number = 7
user_input = input("Please hit 'y' to play: ").lower()

if user_input == 'y':
    user_number = int(input("Please enter number to guess: "))
    if user_number == number:
        print("Your guess perfect number")
    elif abs(number-user_number)==1:
        print("You were off by one")
    else:
        print("Sorry, it's Wrong")