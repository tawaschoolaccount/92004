print("Tane's School Holiday Camp")

#List the camp options
camps_dictionary = {
  "Cultural Immersion":["5 Days","Easy", 800],
  "Kayaking And Pancakes":["3 Days","Moderate", 400],
  "Mountain Biking":["4 Days","Difficult", 900]
}
camps_list = list(camps_dictionary.keys())

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
age = ''
while len(age) == 0 or age.isdigit() == False:
  age = input("Enter your age: ")
  if len(age) == 0: 
    print("You cannot have a blank age")
  if len(age) != 0 and age.isdigit() == False:
    print("Enter a valid number")
camp_number = int(input("Which camp number would you like to go to? "))

#Additional choices
meal_choice = input("Would you like a standard, vegererian, or vegan meal? ").lower()
if meal_choice != "standard" and meal_choice != "vegetarian" and meal_choice != "vegan":
  while meal_choice != "standard" and meal_choice != "vegetarian" and meal_choice != "vegan":
    print("Please enter standard, vegetarian, or vegan")
    meal_choice = input("Would you like a standard, vegererian, or vegan meal? ").lower()
bus_choice = input("Do you need the shuttle bus for an additional $80?(Y/N) ").upper()
if bus_choice != "Y" and bus_choice != "N":
  while bus_choice != "Y" and bus_choice != "N":
    print("Please enter Y or N")
    bus_choice = input("Do you need the shuttle bus for an additional $80?(Y/N) ").upper()
  
#Calculations:
cost = camps_dictionary[camps_list[camp_number - 1]][2]
if bus_choice == "Y": cost += 80

#Final details
print(f"\nHello {name}, you have chosen to go to the {camps_list[camp_number - 1]} (X difficulty) camp for X days. You are {age} years old. Your meal choice is {meal_choice}.")
confirmation = input(f"Please confirm that you want to go to {camps_list[camp_number - 1]} for the cost of ${cost} (Y/N): ").upper()
if confirmation != "Y" and confirmation != "N":
  while confirmation != "Y" and confirmation != "N":
    print("Please enter Y or N")
    confirmation = input(f"Please confirm that you want to go to {camps_list[camp_number - 1]} for the cost of ${cost} (Y/N): ").upper()
if confirmation == "Y": print("Enjoy the camp")
elif confirmation == "N": print("Sorry to hear that, maybe next time")
#note: find a way to get the list of camp details from the dictionary list
