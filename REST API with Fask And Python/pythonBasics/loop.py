#friends = ["Rolf", "Smith", "Anne","Saurabh"]

#for friend in friends:
  #  if friend.startswith("S"):
   #     print(f"{friend} starts with S!")

####################

#grades = [90, 95, 98, 99, 100, 60]
#total = 0

#for grade in grades:
 #   total = total + grade

#average = total / len(grades)  # Not indented, so not part of the loop!
#print(f"Your average grade was {average}.")

#####################

#grades = [90, 95, 98, 99, 100, 60]
#total = sum(grades)
#average = total / len(grades)yes

#print(f"Your average grade was {average}.")
###########

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")