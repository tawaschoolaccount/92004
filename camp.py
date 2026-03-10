print("Tane's School Holiday Camp")
#List the camp options
camps_dictionary = {
  "Cultural Immersion":["5 days","Easy", 800],
  "Kayaking And Pancakes":["3 days","Moderate", 400],
  "Mountain Biking":["4 days","Difficult", 900]
}

camps_list = list(camps_dictionary.keys())
#Number strings to numbers for age input
age_numbers = {
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10,
  "eleven": 11,
  "twelve": 12,
  "thirteen": 13,
  "fourteen": 14,
  "fifteen": 15,
  "sixteen": 16,
  "seventeen": 17,
}

minimum_age = 5
maximum_age = 17
leader_age = 15
camp_numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
}

print("\nThese are the camps, lengths, difficulties, and costs in $:\n")
loop_count = 1
for camp, details_list in camps_dictionary.items():
  print(loop_count, end=': ')
  print(camp, end=' - ')
  for item in details_list:
    print(item, end=' | ')
  print('\n')
  loop_count += 1
  
#Ask user for details
name = input("Enter your name: ")
if len(name) == 0:
  while len(name) == 0:
    print("You cannot have a blank name")
    name = input("Enter your name: ")
age = ''
while len(age) == 0 or age.isdigit() == False or int(age) < minimum_age or int(age) > maximum_age:
  age = input("Enter your age: ")
  if len(age) == 0: 
    print("You cannot have a blank age")
  if len(age) != 0 and age.isdigit() == False:
    if age.lower() in age_numbers:
      age = str(age_numbers[age.lower()])
    else:
      print("Please enter a valid age")
  if len(age) != 0 and age.isdigit() == True and (int(age) < minimum_age or int(age) > maximum_age):
    print("Sorry, you do not meet the age requirements for the camp")
if int(age) >= leader_age:
  leader_choice = input("You are old enough to be a leader, would you like to be a leader for the camp? (Y/N) ").upper()
  if leader_choice != "Y" and leader_choice != "N":
    while leader_choice != "Y" and leader_choice != "N":
      print("Please enter Y or N")
      leader_choice = input("You are old enough to be a leader. Would you like to be a leader for the camp? (Y/N) ").upper()
  if leader_choice == "Y": print("Great, you will be a leader for the camp")
  elif leader_choice == "N": print("No worries, you can still attend the camp as a participant")
    
#Camp choice
camp_number = input("Which camp number would you like to go to? ")
if camp_number not in ["1", "2", "3", "one", "two", "three"]:
  while camp_number not in ["1", "2", "3", "one", "two", "three"]:
    print("Please enter a valid camp number")
    camp_number = input("Which camp number would you like to go to? ")
if camp_number in ["one", "two", "three"]:
  camp_number = camp_numbers[camp_number]
#Meal choice
meal_choice = input("Would you like a standard, vegetarian, or vegan meal? ").lower()
if meal_choice != "standard" and meal_choice != "vegetarian" and meal_choice != "vegan":
  while meal_choice != "standard" and meal_choice != "vegetarian" and meal_choice != "vegan":
    print("Please enter standard, vegetarian, or vegan")
    meal_choice = input("Would you like a standard, vegererian, or vegan meal? ").lower()
    
#Shuttle Bus choice
bus_choice = input("Do you need the shuttle bus for an additional $80?(Y/N) ").upper()
if bus_choice != "Y" and bus_choice != "N":
  while bus_choice != "Y" and bus_choice != "N":
    print("Please enter Y or N")
    bus_choice = input("Do you need the shuttle bus for an additional $80?(Y/N) ").upper()
    
#Calculations:
cost = camps_dictionary[camps_list[camp_number - 1]][2]
if bus_choice == "Y": cost += 80
#Final details
print(f"\nHello {name} ({age}), you have chosen to go to the {camps_list[camp_number - 1]} ({camps_dictionary[camps_list[camp_number - 1]][1]}) camp for {camps_dictionary[camps_list[camp_number - 1]][0]}, and your meal choice is {meal_choice}.")
confirmation = input(f"Please confirm that you want to go to {camps_list[camp_number - 1]} for the cost of ${cost} (Y/N): ").upper()
if confirmation != "Y" and confirmation != "N":
  while confirmation != "Y" and confirmation != "N":
    print("Please enter Y or N")
    confirmation = input(f"Please confirm that you want to go to {camps_list[camp_number - 1]} for the cost of ${cost} (Y/N): ").upper()
if confirmation == "Y": print("Enjoy the camp")
elif confirmation == "N": print("Sorry to hear that, maybe next time")
