#countries = ["Spain", "Italy", "Germany", "United States", "United Kingdom"]
#
#user_country = input("Enter a country you have visited: ")
#
#if user_country in countries:
#    print("I have also visited that country!")
#else:
#   print("I want to go there one day too.")

############

print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, or 'q' to quit: ")

while user_input != "q":
    # Do stuff here

    # At the end of the loop, ask the user whether they want to go again
    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")