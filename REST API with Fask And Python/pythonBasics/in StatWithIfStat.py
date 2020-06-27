movies_watched = {"3idiots","Tere Naam","Chakh De India"}
user_movie = input("Enter movie name: ").lower()

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too!")
else:
    print(f"I didnt watched {user_movie}")