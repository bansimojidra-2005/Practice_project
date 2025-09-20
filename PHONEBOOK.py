#Define the Number of Phonebook
contect = {
    'Ajay':9099785645,
    'Aman':7867563434,
    'Ashish':9878563323,
    'Bina':7990553302,
    'Bimal':9675569099,
    'Bharat':9990448515,
    'Chirag':9987785654,
    'Chetan':6756789045,
    'Dhruv':9067677878,
}

#greet
print("To show the My PHONEBOOK")
print("Ajay: 9099785645\nAman: 7867563434\nAshish: 9878563323\nBina: 7990553302\nBimal: 9675569099\nBharat: 9990448515\nChirag: 9987785654\nChetan: 6756789045\nDhruv: 9067677878")
choice = input("Enter opration (add/search/delete/list) =")
if choice.lower() == "add":
    name = input("Enter name =")
    if name in contect:
        print("This contact alrady exists!") 
    else:
        number = input("Enter number =")
        contect[name] = number
    print(f"Your contect {name} is added successfully!")

#search a contect
search = input("Do you want to search a contect in a phonebook? (Yes/No) =")
if search == "Yes":
    name = input("Enter the name:")

    if name in contect:
        print(name,":",contect[name])
    else:
        print(f"This contect {name} is not found!")

#Delete a contect
del_con = input("Do you want to delete a contect in a phonebook? (Yes/No)")
if del_con == "Yes":
    name = input("Enter the name to delete =")
    if name in contect:
        del contect[name]
        print(f"Contect {name} deletede successfully!")
    else:
        print(f"Contect {name} is not found in phonebook.")
#List to all contects
print("\n My Phonebook Contacts:")
for name,number in contect.items():
    print(name, ":", number)