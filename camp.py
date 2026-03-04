print("Tane's School Holiday Camp")

#List the camp options
camps_dictionary = {
  "Cultural Immersion":["5 Days","Easy", 800],
  "Kayaking And Pancakes":["3 Days","Moderate", 400],
  "Mountain Biking":["4 Days","Difficult", 900]
}

print("\nThese are the activities and costs:")
for item in camps_dictionary:
  print(item)

#Ask user for details
name = input("Enter your name: ")
age = ''
while len(age) == 0 or age.isdigit() == False:
  age = input("Enter your age: ")
  if len(age) == 0: 
    print("You cannot have a blank age")
  if len(age) != 0 and age.isdigit() == False:
    print("Enter a valid number")
camp_number = input("Which camp number would you like to go to? ")

#Extra
meal_choice = input("Would you like a standard, vegererian, or vegan meal? ")
bus_choice = input("Do you need the shuttle bus for an additional $80? ")
