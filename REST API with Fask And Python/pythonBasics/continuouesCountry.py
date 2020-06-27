countries = []

print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, or 'q' to quit: ")

while user_input != "q":
    if user_input == "a":
        name = input("Country name: ")
        countries.append(name)
    elif user_input == "l":
        print(f"You have visited {len(countries)} countries:")
        for country in countries:
            print(f"--> {country}")

    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")