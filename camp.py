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
#notes: format this bit to have less lines

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

#Extra
meal_choice = input("Would you like a standard, vegererian, or vegan meal? ")
bus_choice = input("Do you need the shuttle bus for an additional $80? ")

#final details
print(f"\nHello {name}, you have chosen to go to the {camps_list[camp_number - 1]} (X difficulty) camp for X days. You are {age} years old. Your meal choice is {meal_choice}.")
confirmation = input("Please confirm that you want to go to {camp_number} for the cost of $X (Y/N): ").upper()
if confirmation == "Y": print("Enjoy the camp")
elif confirmation == "N": print("Sorry to hear that, maybe next time")
else:  print("Invalid input, please enter Y or N")
#note: find a way to get the list of camp details from the dictionary list
