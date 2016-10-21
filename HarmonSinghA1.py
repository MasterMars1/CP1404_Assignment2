import csv

"""
Name: Harmon Singh
Date: 9/09/16
Brief Description: This program will effectively perform the actions of a shopping list. Allow the user to add
                   a new item, look at required items, look at completed items and mark an item as completed.
GitHub URL: https://github.com/hamsingh/CP1404.git
"""
__author__ = 'Harmon Singh'
COMPLETED = "c"
REQUIRED = "r"
MENU = "MENU:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"


"""
Psuedo-code: Function load_items
Declaring a new function with the name
Create and empty list
Open CSV file, get it ready to read only and call it file
For each line in the file perform the instructions below
Strip the text and seperate with commas
Convert the item priority located in the third column(column 2) to an integer value
Convert the item price in the second row (column 1) in a floating integer
Add the edited item to the list
Sort the items by the priority
Return the list item_list so it can be accessed by other function outside of this scope
"""


# Load items from csv and put in a list called item_list
def load_items():
    item_list = []
    with open('items.csv', 'r', newline='') as file:
        for item in file.readlines():
            item = item.strip().split(',')
            item[2] = int(item[2])
            item[1] = float(item[1])
            item_list.append(item)
        item_list.sort(key=lambda row: row[2], reverse=False)
    return item_list


# Write list item_list back on the csv file after alterations
def write_items(item_list):
    with open("items.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for item in item_list:
            writer.writerow(item)


# Collect all user inputs for new item and add them to the list item_list
def add_item(item_list):
    item_name = get_item_name()
    item_price = get_item_price()
    item_priority = get_item_priority()
    item_list.append([item_name, item_price, item_priority, 'r'])
    item_list.sort(key=lambda row: row[2], reverse=False)
    print("{}, ${} (priority {}) added to shopping".format(item_name, item_price, item_priority))


# Get name for new item from user
def get_item_name():
    item_name = input("Item name: ")
    invalid_name = True
    while invalid_name:
        if item_name.replace(" ", "") == "":
            print("Item cannot be blank")
            item_name = input("Item name: ")
        else:
            invalid_name = False
    return item_name


# Get price for new item from user
def get_item_price():
    invalid_price = True
    while invalid_price:
        try:
            item_price = float(input("Price: $"))
            if item_price < 0:
                print("Price must be >= $0")
                continue
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            invalid_price = False
    return item_price


# Get priority for new item from user
def get_item_priority():
    invalid_priority = True
    while invalid_priority:
        try:
            item_priority = int(input("Priority: "))
            if item_priority < 1 or item_priority > 3:
                print("Priority must be 1, 2 or 3")
                continue
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            invalid_priority = False
    return item_priority


# Show user all required items
def required_items(item_list):
    print("Required items:")
    total_price = 0
    i = 0
    for item in item_list:
        if REQUIRED in item[3]:
            total_price += item[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, item[0], item[1], item[2]))
            i += 1
    if i == 0:
        print("No required items")
    else:
        print("Total expected price for {} item(s): ${}".format(i, total_price))


"""
Psuedo-code: Function completed_items
Declaring a new function with the name
print Completed items
set the total price to zero to act as total item value counter
set i to zero to act as counter
For each item in item list complete the instructions below
Check if "c" is equal to the third column of the item being checked
If the above is correct then add the price to the total price
Print the information of the item with formatting
Increment i by 1
Test to see if the i value was changed
If it has not print no completed items as this means the above loop didn't run because there where no completed items
If the value i was changed this means there are completed items. Therefore we print the total value of the items
"""


# Show user all completed items
def completed_items(item_list):
    print("Completed items:")
    total_price = 0
    i = 0
    for item in item_list:
        if COMPLETED in item[3]:
            total_price += item[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, item[0], item[1], item[2]))
            i += 1
    if i == 0:
        print("No completed items")
    else:
        print("Total expected price for {} item(s) purchased: ${}".format(i, total_price))


# Show user all required items and enable them to change one from required to completed
def mark_item(item_list):
    print("Required items:")
    total_price = 0
    i = 0
    for item in item_list:
        if REQUIRED in item[3]:
            total_price += item[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, item[0], item[1], item[2]))
            i += 1
    if i == 0:
        print("No required items")
    else:
        print("Total expected price for {} item(s) purchased: ${}".format(i, total_price))
        print("Enter the number of an item to mark as completed")
        invalid_choice = True
        while invalid_choice:
            try:
                change_item = int(input(">>> "))
                if change_item < 0 or change_item > (len(item_list) - 1) or change_item > (i - 1):
                    print("Invalid input; enter a valid number")
                    continue
            except ValueError:
                print("Invalid input; enter a valid number")
            else:
                invalid_choice = False
        for item in item_list:
            if item[3] == COMPLETED:
                item_list.remove(item)
                item_list.append(item)
        for item in item_list:
            if item[3] == "r" and change_item <= (len(item_list) - 1):
                item_list[change_item][3] = "c"
                print("{} marked as completed".format(item_list[change_item][0]))
                item_list.sort(key=lambda row: row[2])
                return item_list


# Main function - Shows menu to user and also keep the whole program running
def main():
    items = load_items()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            required_items(items)
        elif choice == "C":
            completed_items(items)
        elif choice == "A":
            add_item(items)
        elif choice == "M":
            mark_item(items)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    write_items(items)
    number_of_items = len(items)
    print("{} items saved to items.csv".format(number_of_items))
    print("Have a nice day :)")

if __name__ == '__main__':
    main()
